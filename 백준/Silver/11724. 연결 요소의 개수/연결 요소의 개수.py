import sys

def dfs(v):
    stack = [v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(graph[node])

# 입력 받기
n, m = map(int, sys.stdin.readline().split())

# 그래프 초기화
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 그래프 정보 입력 받기
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 요소 개수 구하기
count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

# 결과 출력
print(count)
