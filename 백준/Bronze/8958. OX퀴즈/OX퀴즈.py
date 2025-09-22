def solution(v):
    ansList = []
    
    for i in v:
        num = 0
        ans = 0
        for j in i:
            if j == 'O':
                num += 1
                ans += num
            else:
                num = 0
        ansList.append(ans)

    return ansList

a = int(input())
b = []
for _ in range(a):
    c = input()
    b.append(c)

d = solution(b)

for i in d:
    print(i)