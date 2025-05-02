from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    max_dist = 0

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 'L' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[cx][cy] + 1
                    max_dist = max(max_dist, visited[nx][ny])
                    q.append((nx, ny))
    return max_dist

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            answer = max(answer, bfs(i, j))

print(answer)
