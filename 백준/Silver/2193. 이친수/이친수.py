import sys
input = sys.stdin.readline

N = int(input())

memo = [[0, 0] for _ in range(N+1)]
# [끝자리가 0인 개수, 끝자리가 1인 개수]
memo[1] = [0, 1]

for i in range(2, N+1):
  memo[i][0] = memo[i-1][0] + memo[i-1][1]
  memo[i][1] = memo[i-1][0]

print(memo[N][0] + memo[N][1])