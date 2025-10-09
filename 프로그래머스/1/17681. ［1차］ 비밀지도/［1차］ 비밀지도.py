def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = format(arr1[i] | arr2[i], f'0{n}b')
        tmp = ''
        for i in range(len(num)):
            tmp += '#' if num[i] == '1' else ' '
        answer.append(tmp)
    print(answer)
    return answer