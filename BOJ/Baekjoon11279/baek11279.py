import sys
import heapq

arr = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(arr,(-x,x))
    else:
        if arr:
            num = heapq.heappop(arr)
            print(num[1])
        else:
            print(0)
