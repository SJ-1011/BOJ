student1 = [1, 2, 3, 4, 5]
student2 = [2, 1, 2, 3, 2, 4, 2, 5]
student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    answer = []
    
    num1 = 0
    num2 = 0
    num3 = 0
    
    for i in range(len(answers)):
        if student1[i % 5] == answers[i]:
            num1 += 1
        if student2[i % 8] == answers[i]:
            num2 += 1
        if student3[i % 10] == answers[i]:
            num3 += 1
    
    M = max(num1, num2, num3)
    
    if num1 == M:
        answer.append(1)
    if num2 == M:
        answer.append(2)
    if num3 == M:
        answer.append(3)
        
    return answer