from collections import deque

def solution(n, wires):
    # n: 9
    # wires: [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    
    answer = 999999999
    
    for i in range(len(wires)):
        graph = {}
        wire = wires[:i] + wires[i+1:]
    
        for a, b in wire:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
    
        num = bfs(graph, list(graph.keys())[0])
        answer = min(abs(n - num * 2), answer)
    
    return answer

def bfs(graph, start):
    visit = set()
    queue = deque([start])
    cnt = 0
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visit:
            visit.add(vertex)
            queue.extend([n for n in graph[vertex] if n not in visit])
            cnt += 1
    
    return cnt