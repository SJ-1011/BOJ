def solution(answers):
    # 5 2 3 4 2 / 1 5 1 1
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a_cor = 0
    b_cor = 0
    c_cor = 0
    
    for i in range(len(answers)):
        if answers[i] == a[i % 5]:
            a_cor += 1
        if answers[i] == b[i % 8]:
            b_cor += 1
        if answers[i] == c[i % 10]:
            c_cor += 1
    
    max_cor = max(a_cor, b_cor, c_cor)
    
    answer = [i+1 for i, x in enumerate([a_cor, b_cor, c_cor]) if x == max_cor]
    return answer