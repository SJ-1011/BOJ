N = int(input())
P = list(map(int, input().split(" ")))

sum = 0
P.sort()
for i in range(N):
  for j in range(i+1):
    sum += P[j]
print(sum)