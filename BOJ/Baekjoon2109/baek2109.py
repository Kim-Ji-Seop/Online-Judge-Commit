import sys
import heapq
N = int(sys.stdin.readline())
R = []

arr = [0 for _ in range(N) ]

for i in range(N):    
   arr[i] = list(map(int, sys.stdin.readline().split()))
arr.sort(key=lambda x: (x[1],-x[0]))

for i in range(N):
    heapq.heappush(R,arr[i][0])
    if len(R) > arr[i][1]:
        heapq.heappop(R)
print(sum(R))
