n,k=map(int,input().split())
arr = []
mincnt=0

for i in range(n):
    arr.append(int(input()))

for i in reversed(range(n)):
    mincnt += k // arr[i]
    k = k % arr[i]
print(mincnt)