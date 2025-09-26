from collections import deque

vectors = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(start, target, maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    q = deque()
    sy, sx = start
    q.append((sy, sx, 0))
    visited[sy][sx] = True
    
    while q:
        y, x, dist = q.popleft()
        if maps[y][x] == target:
            return (y, x, dist)
        for dy, dx in vectors:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] != 'X' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, dist+1))
    return None

def solution(maps):
    # 시작 좌표 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i,j)
    
    L_pos = bfs(start, 'L', maps)
    if not L_pos:
        return -1
    
    E_pos = bfs((L_pos[0], L_pos[1]), 'E', maps)
    if not E_pos:
        return -1
    
    return L_pos[2] + E_pos[2]
