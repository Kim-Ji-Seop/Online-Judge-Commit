import sys

n = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().rstrip()))
b_list = list(map(int, sys.stdin.readline().rstrip()))
cnt = 0

def toggle_plus(i):
    for x in range(i, i+2):
        a_list[x] = 1 - a_list[x]
def toggle_minus(i):
    for x in range(i, i-2, -1):
        a_list[x] = 1 - a_list[x]
def toggle(i):
    for x in range(i-1, i+2):
        a_list[x] = 1 - a_list[x]

for i in range(n):
    if a_list != b_list:
        if i == 0:
            toggle_plus(i)
            cnt += 1
        elif i == n-1:
            toggle_minus(i)
            cnt += 1
        else:
            toggle(i)
            cnt += 1
    else:
        break

if a_list == b_list:
    print(cnt)
else:
    print(-1)