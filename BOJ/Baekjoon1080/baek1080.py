import sys

n,m = map(int, sys.stdin.readline().split())

a_list = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
b_list = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
cnt = 0

def toggle(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            a_list[x][y] = 1 - a_list[x][y]

for i in range(n-2):
    for j in range(m-2):
        if i+3 <= n and j+3 <= m:
            if a_list[i][j] != b_list[i][j]:
                toggle(i, j)
                cnt += 1
        if a_list == b_list:
            break
    if a_list == b_list:
        break

if a_list != b_list:
    print(-1)
else:
    print(cnt)