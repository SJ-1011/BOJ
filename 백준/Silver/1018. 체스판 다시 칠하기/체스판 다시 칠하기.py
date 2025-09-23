def solution(n, m, board):
    n1 = 'WBWBWBWB'
    n2 = 'BWBWBWBW'
    ans = 64
    
    for i in range(n - 7):
        for j in range(m - 7):
            num1 = 0 
            num2 = 0 
            for r in range(i, i + 8):
                for c in range(j, j + 8):
                    if r % 2 == 0:
                        if board[r][c] != n1[c % 8]:
                            num1 += 1
                        if board[r][c] != n2[c % 8]:
                            num2 += 1
                    else:
                        if board[r][c] != n2[c % 8]:
                            num1 += 1
                        if board[r][c] != n1[c % 8]:
                            num2 += 1
            ans = min(ans, num1, num2)
    print(ans)


n, m = map(int, input().split())
board = [input() for _ in range(n)]

solution(n, m, board)
