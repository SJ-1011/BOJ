from itertools import permutations

def solution(numbers):
    answer = 0
    ans = []
    for i in range(1, len(numbers)+1):
        ans += permutations(numbers, i)
    ans = set(int(''.join(n)) for n in ans)
    for n in ans:
        if isPrime(n):
            answer += 1        
    return answer

def isPrime(num):
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True