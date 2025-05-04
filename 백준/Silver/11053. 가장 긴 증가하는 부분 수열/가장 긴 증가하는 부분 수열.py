import sys
from itertools import permutations as pm

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

dp = [1] * n  # 최소 LIS 길이는 자기 자신 하나

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
