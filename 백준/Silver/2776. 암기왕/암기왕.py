import sys
input = sys.stdin.readline

# 찾을 리스트와 타겟
def binary_search(arr, target):
  # 왼쪽, 오른쪽 결정 (찾기 위해)
  left, right = 0, len(arr) - 1
  
  while left <= right:
    # 중앙 인덱스
    mid = (left + right) // 2
    if arr[mid] == target:
      return 1
    if arr[mid] < target:
      left = mid + 1
    elif arr[mid] > target:
      right = mid - 1
  return 0

T = int(input())
for _ in range(T):
  N = int(input())
  first_list = list(map(int, input().split(" ")))
  M = int(input())
  second_list = list(map(int, input().split(" ")))
  
  first_list.sort()
  for target in second_list:
    print(binary_search(first_list, target))