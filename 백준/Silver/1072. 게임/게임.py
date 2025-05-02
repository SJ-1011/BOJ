X, Y = map(int, input().split(" "))
num = -1
Z = (Y * 100) // X
left = 0
right = 1_000_000_000
if Z < 99:
  while left <= right:
    mid = (left + right) // 2
    
    # 둘 값이 다르면
    if (Y + mid) * 100 // (X + mid) > Z:
      num = mid
      right = mid - 1
    
    # 같으면
    else:
      left = mid + 1
  
  print(num)

else:
  print(-1)
