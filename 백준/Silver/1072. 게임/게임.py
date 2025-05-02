X, Y = map(int, input().split())
Z = Y * 100 // X

if Z >= 99:
    print(-1)
else:
    left = 1
    right = 1_000_000_000
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        new_z = (Y + mid) * 100 // (X + mid)

        if new_z > Z:
            answer = mid
            right = mid - 1  # 더 작은 답이 있는지 왼쪽 탐색
        else:
            left = mid + 1  # 승률 그대로이므로 오른쪽 탐색

    print(answer)
