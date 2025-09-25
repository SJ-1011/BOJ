def solution(n):
    dp = [0] * (n+1)

    dp[1] = 1
    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 4

        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

T = int(input())
A = []
for i in range(T):
    A.append(int(input()))

for n in A:
    print(solution(n))
    