from collections import deque

def Solution(N):
  queue = deque()
  
  for i in range(1, N+1):
    queue.append(i)
  
  while len(queue) > 1:
    queue.popleft()

    if len(queue) <= 1:
      break
    else:
      queue.append(queue.popleft())

  return queue[0]

N = int(input())

print(Solution(N))