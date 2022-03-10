t = int(input()) # test case

while t > 0:
    count = 0
    n, idx = map(int, input().split()) # n = 문서의 개수 / idx = 배열에서의 위치(index)
    priority = list(map(int, input().split())) # 문서 중요도 나열
    list_w = [0] * n
    list_w[idx] = 1
#   ---------------------사전 준비 -----------------------
    while True:
        if priority[0] == max(priority):
            count += 1
            if list_w[0] == 1:
                print(count)
                break
            else:
                del priority[0]
                del list_w[0]
        else:
            priority.append(priority[0])
            list_w.append(list_w[0])
            del priority[0]
            del list_w[0]
    t -= 1
