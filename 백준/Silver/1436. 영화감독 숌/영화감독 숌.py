def solution(num):
    ans = 666
    a = 0
    while True:
        if '666' in str(ans):
            a += 1
        if num == a:
            return ans
        ans += 1

a = int(input())
print(solution(a))