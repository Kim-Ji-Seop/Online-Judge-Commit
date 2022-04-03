from sys import stdin
from collections import deque


M,N,H = map(int,stdin.readline().split())
graph = [[list(map(int, stdin.readline().split())) for _ in range(M)] for _ in range(H)]
for i in range(M*H):
    for j in range(N):
        graph[i][j]
cnt = 0
X = [-1,1,0,0,0,0]
Y = [0,0,-1,1,0,0]
Z = [0,0,0,0,-1,1]
print(graph)
# def BFS():
#     global cnt
#     queue = deque()
#     for i in range(M):
#         for j in range(N):
#             for k in range(H):
#                 if graph[i][j][k] == 1:
#                     queue.append((i,j,k))
    
#     while queue:
#         x, y, z = queue.popleft()
#         for i in range(6):
#             nx = x + X[i]
#             ny = y + Y[i]
#             nz = z + Z[i]
#             if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H:
#                 continue
#             if graph[nx][ny][nz] == -1:
#                 continue
#             if graph[nx][ny][nz] == 0:
#                 graph[nx][ny][nz] = graph[x][y][z] + 1
#                 queue.append((nx,ny,nz))
            
    

# BFS()
# for i in graph:
#     for j in i:
#         if j == 0:
#             print(-1)
#             exit(0)
#     cnt = max(cnt,max(i))
# print(cnt - 1)