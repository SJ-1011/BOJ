import sys
input = sys.stdin.readline

memo0 = [0] * 41
memo1 = [0] * 41

memo0[0] = 1
memo1[0] = 0
memo0[1] = 0
memo1[1] = 1

for i in range(2, 41):
  memo0[i] = memo0[i-1] + memo0[i-2]
  memo1[i] = memo1[i-1] + memo1[i-2]

T = int(input())
for _ in range(T):
  n = int(input())
  print(memo0[n], memo1[n])