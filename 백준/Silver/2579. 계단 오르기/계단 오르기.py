import sys
input = sys.stdin.readline

stair = int(input())
points = [0]
for _ in range(stair):
    num = int(input())
    points.append(num)

dp = [0] * (stair + 1)

dp[1] = points[1]

if stair > 1:
    dp[2] = points[1] + points[2]

    if stair > 2:
        dp[3] = max(points[1] + points[3], points[2] + points[3])

        for i in range(4, stair + 1):
            dp[i] = max(dp[i-2] + points[i], dp[i-3] + points[i-1] + points[i])

print(dp[stair])