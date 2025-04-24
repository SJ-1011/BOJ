import sys
from itertools import permutations as pm
input = sys.stdin.readline

N = int(input())
num = 0

lines = []
for _ in range(N):
  lines.append(list(map(int, input().split(" "))))

answer = [list(p) for p in pm(range(1, 10), 3)]

def check(ans, question, s, b):
  strike, ball = 0, 0
  for i in range(3):
    if int(ans[i]) == int(question[i]):
      strike += 1
    elif int(question[i]) in ans:
      ball += 1
  return strike == s and ball == b

for ans in answer:
  isPossible = True
  # ans = [1, 2, 3]
  for quest, s, b in lines:
    # quest = "123"
    if not check(ans, str(quest), s, b):
      isPossible = False
      break
  if isPossible:
    num += 1

print(num)