import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split(" "))) for _ in range(N)]

# 플로이드–워셜: 누적 갱신 알고리즘
for k in range(N):
  # k는 중간 지점
  for i in range(N):
    # i는 시작 지점
    for j in range(N):
      # j는 도착 지점
      if graph[i][k] and graph[k][j]:
        graph[i][j] = 1

for row in graph:
  print(*row)