def Solution(s):
  pairs = {
  '(': ')'
  }
  stack = []

  for char in s:
    if char in pairs:
      stack.append(char)
    else:
      if not stack or pairs[stack.pop()] != char:
        return False
  return len(stack) == 0


T = int(input())

lines = []
for _ in range(T):
  lines.append(input())

for line in lines:
  print('YES' if Solution(line) else 'NO')