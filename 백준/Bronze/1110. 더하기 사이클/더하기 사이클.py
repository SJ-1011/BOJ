def solution(N):
    str_N = str(N)
    if len(str_N) == 1:
        str_N = '0' + str_N
    res = str_N[1] + str(int(str_N[0]) + int(str_N[1]))[-1]
    cl = 1
    while int(res) != N:
        str_res = str(res)
        if len(str_res) == 1:
            str_res = '0' + str_res
        
        res = str_res[1] + str(int(str_res[0]) + int(str_res[1]))[-1]
        cl += 1
    return cl
N = int(input())
print(solution(N))