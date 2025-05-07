import sys
from collections import deque

def bfs(N, M, area, x, y):
  queue = deque()
  if area[y][x] != 0:
    return False
  area[y][x] = 1
  count = 1
  queue.append((x, y))
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  while queue:
    cx, cy = queue.popleft()
    for direct in range(4):
      nx = cx + dx[direct]
      ny = cy + dy[direct]
      if 0 <= nx < N and 0 <= ny < M:
        if area[ny][nx] == 0:
          area[ny][nx] = 1
          queue.append((nx, ny))
          count += 1
  return count

input = sys.stdin.readline

M, N, K = map(int, input().split(" "))
rect = [list(map(int, input().split(" "))) for _ in range(K)]
area = [[0] * N for _ in range(M)]

for r in rect:
  for y in range(r[1], r[3]):
    for x in range(r[0], r[2]):
      area[M-y-1][x] = 1

answer = []

for y in range(M):
  for x in range(N):
    ans = bfs(N, M, area, x, y)
    if ans:
      answer.append(ans)

answer.sort()
print(len(answer))
print(*answer)