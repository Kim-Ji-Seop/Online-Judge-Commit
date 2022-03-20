import sys
B =int(sys.stdin.readline())
arr = [0 for _ in range(B) ]
for i in range(B):    
	arr[i] = list(map(int, sys.stdin.readline().split()))

arr.sort(key = lambda x: (x[1],x[0]))
count=1
endT = arr[0][1]
for i in range(1,B):
    if endT <= arr[i][0]:
        endT = arr[i][1]
        count += 1
print(count)