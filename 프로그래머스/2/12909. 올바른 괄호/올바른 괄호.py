def solution(s):
    
    stack = []
    answer = True
    
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack != []:
                stack.pop()
            else:
                answer = False
                break
    
    if stack != []:
        answer = False
    
    return answer