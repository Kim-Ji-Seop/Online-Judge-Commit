from sys import stdin
from collections import deque


N,M = map(int,stdin.readline().split())

graph = [list(map(int, stdin.readline().split())) for _ in range(M)]
cnt = 0
X = [-1,1,0,0]
Y = [0,0,-1,1]

def BFS():
    global cnt
    queue = deque()
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                queue.append((i,j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
            
    

BFS()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt,max(i))
print(cnt - 1)