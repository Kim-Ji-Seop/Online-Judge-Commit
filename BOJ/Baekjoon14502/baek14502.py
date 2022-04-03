from sys import stdin
from collections import deque
import copy

N,M = map(int,stdin.readline().split())

graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
max_value = 0


X = [-1,1,0,0]
Y = [0,0,-1,1]

def BFS():
    global max_value
    tmp = copy.deepcopy(graph)
    cnt = 0
    queue = deque()
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                queue.append((nx,ny))
    
    for i in range(N):
        cnt += tmp[i].count(0)
    
    max_value = max(max_value,cnt)

def make_wall(start,cnt):
    if cnt == 3:    
        BFS()
        return
    # for i in range(N):
    #     for j in range(M):
    #         if graph[i][j] == 0:
    #             graph[i][j] = 1
    #             make_wall(cnt+1)
    #             graph[i][j] = 0
    for i in range(start,N*M):
        x = i // M
        y = i % M
        if graph[x][y] == 0:
            graph[x][y] = 1
            make_wall(i,cnt+1)
            graph[x][y] = 0



make_wall(0,0)
print(max_value)
