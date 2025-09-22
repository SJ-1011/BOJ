def solution(v):
    for i in range(v):
        s = i + sum(int(d) for d in str(i))
        if s == v:
            return i
    return 0

i = int(input())
print(solution(i))