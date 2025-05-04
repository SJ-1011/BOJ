import sys
from itertools import combinations as cb

input = sys.stdin.readline
stair = int(input())
score = [0]
for _ in range(stair):
  score.append(int(input()))
  
memo = [0] * (stair+1)

if stair == 1:
  print(score[1])
elif stair == 2:
  print(max(score[1] + score[2], score[2]))
else:
  # 첫 계단
  memo[1] = score[1]
  # 두 번째 계단
  memo[2] = max(score[1] + score[2], score[2])
  # 세 번째 계단
  memo[3] = max(score[1] + score[3], score[2] + score[3])

  for i in range(4, stair + 1):
    memo[i] = max(memo[i - 2] + score[i], memo[i - 3] + score[i - 1] + score[i])

  print(memo[stair])