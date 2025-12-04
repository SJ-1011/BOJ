A = int(input())
B = int(input())
C = int(input())

res = A * B * C
res_str = str(res)
ans = [0 for _ in range(10)]

for c in res_str:
    ans[int(c)] += 1

for num in ans:
    print(num)
