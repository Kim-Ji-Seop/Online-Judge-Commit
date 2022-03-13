import sys
import heapq

arr = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(arr,x)
    else:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)