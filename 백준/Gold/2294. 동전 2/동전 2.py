import sys

input = sys.stdin.readline
n, k = map(int, input().split(" "))

coins = [int(input()) for _ in range(n)]

# 사용한 동전의 개수 min
memo = [99999999] * (k+1)
memo[0] = 0 # 아무것도 사용하지 않음

for i in range(1, k+1):
  if i in coins:
    memo[i] = 1
  else:
    # [2, 5, 12]
    for coin in coins:
      if i > coin:
        memo[i] = min(memo[i - coin] + 1, memo[i])

print(memo[k] if memo[k] != 99999999 else -1)     