import sys
import heapq
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    heapq.heappush(heap,x)

for _ in range(n):
    print(heapq.heappop(heap))