import itertools
def solution(numbers):
    # 4367
    s = set()
    answer = 0
    
    for i in range(1, len(numbers)+1):
        for t in itertools.permutations(numbers, i):
            num = int(''.join(t))
            s.add(num)
            
    for num in s:
        if isPrime(num):
            answer += 1
        
    return answer

def isPrime(num):
    if num == 2:
        return True
    if num == 1 or num == 0:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True