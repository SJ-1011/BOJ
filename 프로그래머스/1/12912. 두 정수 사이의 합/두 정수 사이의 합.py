def solution(a, b):
    A = max(a, b)
    B = min(a, b)
    answer = 0
    for i in range(B, A+1):
        answer += i
    return answer