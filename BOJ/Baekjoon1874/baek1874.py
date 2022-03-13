n = int(input())
stack = [] #stack에 들어갈 숫자 리스트
command = [] #정답 +와 -기호가 들어갈 리스트
start = 1 #숫자가 늘어나면서 target_number와 비교될 숫자.
toggle = 0
for _ in range(n):
    target_number = int(input())
    while start <= target_number:
        command.append('+')
        stack.append(start)
        start += 1

    if stack[-1] == target_number:
        command.append('-')
        del stack[-1]
    else:
        toggle = 1

if toggle == 0:
    for i in command:
        print(i)
else:
    print("NO")
    