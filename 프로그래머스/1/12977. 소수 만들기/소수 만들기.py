from itertools import combinations
import math
def solution(nums):
    answer = 0

    for comb_num in combinations(nums, 3):
        if is_prime(sum(comb_num)):
            answer += 1
    
    return answer

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True