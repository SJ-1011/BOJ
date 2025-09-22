from itertools import combinations

def solution(M, L):
    ans = 0
    L = list(map(int, L))
    a = list(combinations(L, 3))

    for i in a:
        k = sum(i)
        if k <= M:
            ans = max(ans, k)

    return ans

a, b = input().split(' ')
c = input().split(' ')
print(solution(int(b), c))