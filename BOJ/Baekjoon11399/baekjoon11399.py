n = int(input())
a = [int(n) for n in input().split()]
sum=0
tmp = 0
a.sort()
for i in a:
    tmp += i
    sum += tmp
print(sum)