from itertools import combinations

def solution(relation):
    answer = 0
    attribute = [x for x in range(len(relation[0]))]
    comb = []
    for i in range(1, len(attribute)+1):
        comb.extend(list(combinations(attribute, i)))
    
    suc = []
    
    for com in comb:
        s = []
        b = True
        conti = True
        
        for i in range(len(suc)):
            tmp1 = set(suc[i])
            tmp2 = set(com)
            if len(tmp2 - tmp1) == len(tmp2) - len(tmp1):
                conti = False
                break
                
        if conti == True:
            for i in range(len(relation)):
                t = ()
                for elem in com:    
                    t += (relation[i][elem],)
                if t in s:
                    b = False
                    break
                else:
                    s.append(t)

            if b == True:
                answer += 1
                suc.append(com)
    
    return answer