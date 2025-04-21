from collections import deque
def Solution(data):
  q = deque(range(data[0]))
  ans = []
  
  while q:
    if data[2][0] == max(data[2]):
      ans.append(q.popleft())
      data[2].pop(0)
    else:
      q.append(q.popleft())
      data[2].append(data[2].pop(0))
  
  return ans.index(data[1])

T = int(input())

inputlist = []
for _ in range(T):
  N, M = map(int, input().split(" "))
  priority = list(map(int, input().split(" ")))
  inputlist.append([N, M, priority])
  
for i in range(T):
  answer = Solution(inputlist[i])
  print(answer + 1)