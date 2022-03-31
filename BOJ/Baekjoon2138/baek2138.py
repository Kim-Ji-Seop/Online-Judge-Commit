import sys

n = int(sys.stdin.readline())
before = list(map(int, sys.stdin.readline().rstrip()))
after = list(map(int, sys.stdin.readline().rstrip()))


def start(count):
    temp = count
    temp_arr = before[:]
    if temp == 1:
        temp_arr[1] = 1 - temp_arr[1]
        temp_arr[0] = 1 - temp_arr[0]
    for i in range(1,n):
        if temp_arr[i-1] != after[i-1]:
            temp += 1
            temp_arr[i-1] = 1 - temp_arr[i-1]
            temp_arr[i] = 1 - temp_arr[i]
            if i != n-1:
                temp_arr[i+1] = 1 - temp_arr[i+1]
    if temp_arr == after:
        return temp
    else:
        return -1
            
con1 = start(0)
con2 = start(1)

if con1 >= 0 and con2 >= 0:
    print(min(con1,con2))
elif con1 < 0 and con2 >= 0:
    print(con2)
elif con1 >= 0 and con2 < 0:
    print(con1)
else:
    print(-1)


