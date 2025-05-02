import sys
from itertools import combinations as cb
from collections import deque
input = sys.stdin.readline

N = int(input())
team = []
for i in range(N):
  team.append(list(map(int, input().split(" "))))
  
sp = list(cb([x+1 for x in range(N)], N//2))
queue = deque()

for s in sp:
  cbij = list(cb(s, 2))
  sum = 0
  for ij in cbij:
    sum += team[ij[0]-1][ij[1]-1]
    sum += team[ij[1]-1][ij[0]-1]
  queue.append(sum)

val = 9999999999

while queue:
  first_val = queue.popleft()
  last_val = queue.pop()
  
  val = min(val, abs(first_val - last_val))
  
print(val)