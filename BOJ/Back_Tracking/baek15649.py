from sys import stdin
# 백트래킹 연습
N,M = map(int,stdin.readline().split())

graph = []

def BT():
    if len(graph) == M:
        print(' '.join(map(str,graph)))
        return
    for i in range(1,N+1):
        if i not in graph:
            graph.append(i)
            BT()
            graph.pop()
BT()