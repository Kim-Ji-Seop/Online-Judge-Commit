from sys import stdin
# 백트래킹 연습



N,M = map(int,stdin.readline().split())

graph = []

def BT(s):
    if len(graph) == M:
        print(' '.join(map(str,graph)))
        return
    for i in range(s,N+1):
        graph.append(i)
        BT(i)
        graph.pop()
BT(1)