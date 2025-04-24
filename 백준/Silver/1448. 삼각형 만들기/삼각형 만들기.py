import sys
input = sys.stdin.readline

N = int(input())
triangles = [int(input()) for _ in range(N)]
triangles.sort(reverse=True)

answer = -1

for i in range(len(triangles) - 2):
  if triangles[i+1] + triangles[i+2] > triangles[i]:
    answer = triangles[i+1] + triangles[i+2] + triangles[i]
    break
    
print(answer)