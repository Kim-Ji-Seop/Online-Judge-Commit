from sys import stdin
from collections import deque


M,N,H = map(int,stdin.readline().split())
graph = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)]

cnt = 0
X = [-1,1,0,0,0,0]
Y = [0,0,-1,1,0,0]
Z = [0,0,0,0,-1,1]


                    
def BFS():
    global cnt
    queue = deque()
    for i in range(H): #z
        for j in range(N): #x
            for k in range(M): #y
                if graph[i][j][k] == 1:
                    queue.append((i,j,k))
    
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + Z[i]
            nx = x + X[i]
            ny = y + Y[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                continue
            if graph[nz][nx][ny] == -1:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz,nx,ny))

BFS()
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        cnt = max(cnt,max(j))
print(cnt - 1)
