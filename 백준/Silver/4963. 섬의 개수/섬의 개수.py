import sys
from collections import deque

# 8방향 (상, 하, 좌, 우, 대각선들)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

input = sys.stdin.readline

def bfs(x, y):
  visit[x][y] = True
  queue = deque()
  queue.append((x, y))
  
  while queue:
    # 현재 x, y 좌표
    cx, cy = queue.popleft()
    for direction in range(8):
      # 다음 x, y 좌표
      nx = cx + dx[direction]
      ny = cy + dy[direction]
      if 0 <= nx < h and 0 <= ny < w:
        if not visit[nx][ny] and graph[nx][ny] == 1:
          visit[nx][ny] = True
          queue.append((nx, ny))



while True:
  w, h = map(int, input().split(" "))
  
  if w == 0 and h == 0:
    break
  
  graph = []
  for i in range(h):
    graph.append(list(map(int, input().split(" "))))
  
  visit = [[False] * w for _ in range(h)]
  count = 0
  
  for i in range(h):
    for j in range(w):
      # 해당 노드가 land(1)이고, 방문하지 않았을 때,
      # 너비우선탐색 시작
      if graph[i][j] == 1 and not visit[i][j]:
        bfs(i, j)
        count += 1
  print(count)
