def solution(brown, yellow):
    # 8 * 2 + 6 * 2 - 4 = 24(테두리)
    
    size = brown + yellow
    nums = []
    answer = []
    
    for i in range(1, size+1):
        if size % i == 0:
            nums.append([i, int(size / i)])
    
    for num in nums:
        if num[0] * 2 + num[1] * 2 - 4 == brown:
            if num[0] < num[1]:
                num[0], num[1] = num[1], num[0]
            answer.append(num)

    return answer[0]