import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, graph, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for next_node in sorted(graph[start]):
        if next_node not in visited:
            result.extend(dfs(next_node, graph, visited))
    return result

def bfs(start, graph):
    queue = deque([start])
    visited = set([start])
    result = [start]
    while queue:
        node = queue.popleft()
        for next_node in sorted(graph[node]):
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
                result.append(next_node)
    return result

print(*dfs(V, graph))
print(*bfs(V, graph))
