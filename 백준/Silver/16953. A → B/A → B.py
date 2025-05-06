import sys
from collections import deque

def bfs(A, B):
  queue = deque()
  queue.append((A, 0))
  
  countList = []

  while queue:
    na, count = queue.popleft()
    if na == B:
      return count + 1
    if na * 2 <= B:
      queue.append((na * 2, count + 1))
    if na * 10 + 1 <= B:
      queue.append((na * 10 + 1, count + 1))
      
  return -1

input = sys.stdin.readline
A, B = map(int, input().split(" "))

result = bfs(A, B)
print(result)