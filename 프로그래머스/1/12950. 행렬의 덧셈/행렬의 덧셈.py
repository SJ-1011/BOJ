def solution(arr1, arr2):
    num = len(arr1)
    num2 = len(arr1[0])
    answer = [[] for _ in range(num)]
    
    for i in range(num):
        for j in range(num2):
            answer[i].append(arr1[i][j] + arr2[i][j])
    
    return answer