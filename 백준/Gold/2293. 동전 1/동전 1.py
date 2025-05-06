import sys

input = sys.stdin.readline
n, k = map(int, input().split(" "))

coins = [int(input()) for _ in range(n)]

# n원을 만드는 경우의 수
memo = [0] * (k+1)
memo[0] = 1 # 아무것도 안 쓰는 방법 1가지

for coin in coins:
  for i in range(coin, k+1):
    memo[i] += memo[i - coin]
    
print(memo[k])