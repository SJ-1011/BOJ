import sys
from collections import deque

# BFS 수행
def bfs(graph, x, y, m, n):
  if graph[y][x] == 0:
    return False
  queue = deque()
  queue.append((x, y))
  count = 1
  graph[y][x] = 0
  
  # move
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  
  while queue:
    cx, cy = queue.popleft()
    for direct in range(4):
      nx = cx + dx[direct]
      ny = cy + dy[direct]
      
      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] == 1:
          queue.append((nx, ny))
          count += 1
          graph[ny][nx] = 0
  
  return count


input = sys.stdin.readline

n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

max_ans = 0
cnt = 0
for y in range(n):
  for x in range(m):
    ans = bfs(graph, x, y, m, n)
    if ans != False:
      cnt += 1
      max_ans = max(max_ans, ans)

print(cnt)
print(max_ans)