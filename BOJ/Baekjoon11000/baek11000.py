import sys
import heapq

N = int(sys.stdin.readline())
classRoom = []
arr = [0 for _ in range(N) ]
for i in range(N):    
	arr[i] = list(map(int, sys.stdin.readline().split()))
arr.sort(key=lambda x: x[0])
heapq.heappush(classRoom,arr[0][1])
for i in range(1,N):
    if arr[i][0] < classRoom[0]:
        heapq.heappush(classRoom,arr[i][1])
    else:
        heapq.heappop(classRoom)
        heapq.heappush(classRoom,arr[i][1])
print(len(classRoom))