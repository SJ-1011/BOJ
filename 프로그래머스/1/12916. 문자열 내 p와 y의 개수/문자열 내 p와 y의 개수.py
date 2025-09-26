def solution(s):
    answer = True
    
    s = s.upper()
    p, y = 0, 0
    for c in s:
        if c == 'P':
            p += 1
        elif c == 'Y':
            y += 1
    
    if p != y:
        answer = False

    return answer