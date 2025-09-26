def solution(n, lost, reserve):
    
    lost_only = [x for x in lost if x not in reserve]
    reserve_only = [x for x in reserve if x not in lost]

    for r in sorted(reserve_only):
        if r-1 in lost_only:
            lost_only.remove(r-1)
        elif r+1 in lost_only:
            lost_only.remove(r+1)
    
    answer = n - len(lost_only)
    return answer