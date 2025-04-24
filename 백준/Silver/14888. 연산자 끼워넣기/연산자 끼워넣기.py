import sys
from itertools import permutations as pm
input = sys.stdin.readline

# [] 안에 '+', '-' 뭐 이런거 순열로 삽입
# 하나씩 꺼내서 계산

N = int(input())
num = list(map(int, input().split(" ")))
cal = list(map(int, input().split(" ")))
symbol = []
answer = []

for i in range(cal[0]):
  symbol.append('+')
for i in range(cal[1]):
  symbol.append('-')
for i in range(cal[2]):
  symbol.append('*')
for i in range(cal[3]):
  symbol.append('/')
  
tmps = set(pm(symbol, N-1))

for tmp in tmps:
  change = num[0]
  for i in range(1, len(num)):
    if tmp[i-1] == '+':
      change += num[i]
    elif tmp[i-1] == '-':
      change -= num[i]
    elif tmp[i-1] == '*':
      change *= num[i]
    elif tmp[i-1] == '/':
      change /= num[i]
      change = int(change)
  answer.append(change)


print(max(answer))    
print(min(answer))    