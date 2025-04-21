def Solution(N, K):
  queue = [i for i in range(1, N+1)]
  p = -1
  ans = []
  
  while queue:
    p = (p + K) % len(queue)
    ans.append(queue.pop(p))
    p -= 1
    
  return ans

N, K = map(int, input().split(" "))
answer = Solution(N, K)

print(f"<{', '.join(map(str, answer))}>")