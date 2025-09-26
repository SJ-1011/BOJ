import math
def solution(brown, yellow):
    answer = []
    
    full = brown + yellow
    
    nums = []
    for i in range(1, int(math.sqrt(full)) + 1):
        if (brown + yellow) % i == 0:
            nums.append([i, full // i])
    
    for num in nums:
        num.sort()
        if (num[0] - 2) * (num[1] - 2) == yellow:
            answer = [num[1], num[0]]
            break
    
    
    return answer