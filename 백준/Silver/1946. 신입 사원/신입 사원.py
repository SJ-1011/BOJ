import sys
input = sys.stdin.readline

T = int(input())
answer = []

for _ in range(T):
    N = int(input())
    testCase = [tuple(map(int, input().split())) for _ in range(N)]
    testCase.sort()  # 서류 등수 기준으로 오름차순 정렬

    num = 1
    rank = testCase[0][1]  # 첫 번째 면접 등수 (서류 1등)

    for i in range(1, N):
        if testCase[i][1] < rank:
            num += 1
            rank = testCase[i][1]

    answer.append(num)

for ans in answer:
    print(ans)
