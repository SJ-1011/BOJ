import sys

input = sys.stdin.readline
N, M = map(int, input().split(" "))
num = 0

S = []
for _ in range(N):
  S.append(input().strip())

checks = []
for _ in range(M):
  checks.append(input().strip())
  
found = False

# 정렬 시키고, 둘로 나눠서 비교
S.sort()
left = 0
right = len(S) - 1

for check in checks:
  left = 0
  right = len(S) - 1
  while left < right:
    mid = (left + right) // 2
    
    if check in S[mid][:len(check)] or check in S[left][:len(check)] or check in S[right][:len(check)]:
      num += 1
      break
    elif check > S[mid]:
      left = mid + 1
    else:
      right = mid - 1
    
print(num)