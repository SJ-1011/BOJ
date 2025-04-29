import sys

def bfs(x, y):
    # 시작 위치 x y, 총 움직인 거리 1
    queue = [[[x, y], 1]]
    # 방문한 위치 저장
    num = x + y * m
    visit = set([num])
    front = 0
    rear = 1

    # 큐가 비어있지 않을때
    while front < rear:
        pos, ans = queue[front]
        front += 1
        
        next_pos = [[pos[0] + 1, pos[1]], [pos[0] - 1, pos[1]], [pos[0], pos[1] + 1], [pos[0], pos[1] - 1]]
        for next in next_pos:
            y = next[0]
            x = next[1]
            if 0 <= y < n and 0 <= x < m:
                num = x + y * m
                if num not in visit:
                    if maze[y][x] == '1':
                        visit.add(num)
                        queue.append([next, ans + 1])
                        rear += 1
                        if x == m-1 and y == n-1:
                            return ans + 1
    return ans






n, m = map(int, input().split())
maze = []
for _ in range(n):
    s = list(sys.stdin.readline())
    s.pop()
    maze.append(s.copy())

result = bfs(0, 0)
print(result)