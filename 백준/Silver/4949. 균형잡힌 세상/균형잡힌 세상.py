def Solution(data):
  pair = {
    '(': ')',
    '[': ']'
  }
  stack = []
  
  for char in data:
    if char == '(' or char == ')' or char == '[' or char == ']':
      if char in pair:
        stack.append(char)
      else:
        if not stack or pair[stack.pop()] != char:
          return 'no'
  return 'yes' if not stack else 'no'

textList = []
text = input()
textList.append(text)
while text != ".":
  text = input()
  textList.append(text)
textList.pop()

for text in textList:
  print(Solution(text))