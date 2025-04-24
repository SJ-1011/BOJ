import sys
from itertools import combinations as cb
input = sys.stdin.readline

N, S = map(int, input().split(" "))
quest = list(map(int, input().split(' ')))
answer = 0

for r in range(1, N+1):
  tmp = list(cb(quest, r))
  for t in tmp:
    if sum(t) == S:
      answer += 1
print(answer)