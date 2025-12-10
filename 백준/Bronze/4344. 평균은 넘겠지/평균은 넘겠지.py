C = int(input())

ans = []
lst = []
for _ in range(C):
    tmp = input().split()
    lst.append(tmp)

for elem in lst:
    cnt = 0
    sum = 0
    for i in range(1, len(elem)):
        sum += int(elem[i])
    avg = sum / int(elem[0])
    for i in range(1, len(elem)):
        if int(elem[i]) > avg:
            cnt += 1
    ans.append(format(cnt / int(elem[0]) * 100, ".3f"))
    # print(avg, cnt)

for a in ans:
    print(f"{a}%")