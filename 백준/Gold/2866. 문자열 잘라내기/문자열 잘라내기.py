import sys

input = sys.stdin.readline
R, C = map(int, input().split(" "))
table = []

for _ in range(R):
  table.append(list(input().strip()))
count = 0
left = 0
right = R

while left <= right:
  mid = (left + right) // 2
  newTable = table[mid:]
  repet = set()
  for i in range(C):
    repet.add(''.join(newTable[j][i] for j in range(len(newTable))))

  
  if len(repet) < C:
    right = mid - 1
  else:
    count = mid
    left = mid + 1

print(count)