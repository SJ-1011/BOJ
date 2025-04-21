def Solution(datas):
  stack = []
  ans = []
  
  # 스택의 최상위 요소 위치
  top = -1
  
  # 오름차순으로 증가하는 수
  num = 1
  
  # 입력된 수열을 전부 사용할 때까지
  while datas:
    # 스택에 들어갈 수가 data보다 작거나 같을 경우 스택에 추가가
    if num <= datas[0]:
      stack.append(num)
      top += 1
      num += 1
      ans.append('+')
    # 스택에 들어갈 수가 data보다 큰 경우 stack[top] 제거거
    else:
      if stack[top] == datas[0]:
        stack.pop()
        datas.pop(0)
        top -= 1
        ans.append('-')
      # stack[top]이 datas[0]과 같지 않다면,
      # 현 상황에서 push를 하든 pop을 하든 진행이 되지 않기에 NO 리턴
      else:
        return 'NO'
  return ans

# n개의 데이터
n = int(input())

# 입력 데이터가 담긴 리스트
datas = []
for _ in range(n):
  datas.append(int(input()))

answer = Solution(datas)
if answer != "NO":
  for i in range(len(answer)):
    print(answer[i])
else:
  print(answer)