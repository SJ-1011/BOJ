def solution(arr):
    answer = []
    
    stack = [-1]
    for elem in arr:
        if elem != stack[-1]:
            stack.append(elem)
            answer.append(elem)
    
    return answer