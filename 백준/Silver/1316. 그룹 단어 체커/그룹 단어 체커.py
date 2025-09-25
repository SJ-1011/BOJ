import sys

input = sys.stdin.readline
n = int(input())
T = [input().strip() for _ in range(n)]

ans = n
for word in T:
    tmp = []
    for i in range(len(word)):
        if word[i] not in tmp:
            tmp.append(word[i])
        else:
            if tmp[-1] == word[i]:
                tmp.append(word[i])
            else: 
                ans -= 1
                break

print(ans)