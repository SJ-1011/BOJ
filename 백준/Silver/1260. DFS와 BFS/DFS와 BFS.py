from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, v = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited_bfs = [False] * (n + 1)
visited_dfs = [False] * (n + 1)

def bfs(start):
    ans = [start]
    q = deque()
    q.append(start)
    visited_bfs[start] = True
    
    while q:
        cv = q.popleft()
        for nxt in graph[cv]:
            if visited_bfs[nxt] == False:
                q.append(nxt)
                ans.append(nxt)
                visited_bfs[nxt] = True
    
    return ans

ans_dfs = []
def dfs(start):
    visited_dfs[start] = True
    ans_dfs.append(start)
    for nxt in graph[start]:
        if visited_dfs[nxt] == False:
            dfs(nxt)

dfs(v)
ans_bfs = bfs(v)

for i in range(len(ans_dfs)):
    print(ans_dfs[i], end=' ')

print()
for i in range(len(ans_bfs)):
    print(ans_bfs[i], end=' ')