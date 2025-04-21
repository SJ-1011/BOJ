def Solution(data):
  sum = 0
  ans = []
  for i in range(len(data)):
    if data[i] != 0:
      ans.append(data[i])
    else:
      ans.pop()
  
  for i in range(len(ans)):
    sum += ans[i]
      
  return sum


K = int(input())

inputlist = []
for _ in range(K):
  inputlist.append(int(input()))

print(Solution(inputlist))