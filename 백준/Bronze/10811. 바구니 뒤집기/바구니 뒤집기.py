N, M = map(int, input().split())
L = [x + 1 for x in range(N)]
for turn in range(M):
    i, j = map(int, input().split())
    L_mini = L[i-1:j]
    L_mini.reverse()
    L[i-1:j] = L_mini

for i in range(N):
    print(L[i], end = ' ')