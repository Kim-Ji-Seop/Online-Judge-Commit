import sys
import heapq

arr = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(arr,(abs(x),x))
    else:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)