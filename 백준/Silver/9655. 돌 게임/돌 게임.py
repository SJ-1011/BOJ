import sys
input = sys.stdin.readline

N = int(input())

# 상근이 기준
memo = [True] * 1001

memo[1] = True
memo[2] = False
memo[3] = True
memo[4] = False

for i in range(5, 1001):
  memo[i] = not memo[i-1]

print("SK" if memo[N] else "CY")