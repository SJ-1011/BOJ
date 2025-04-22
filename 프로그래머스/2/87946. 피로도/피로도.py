import itertools
def solution(k, dungeons):
    answer = 0
    d = [list(p) for p in itertools.permutations(dungeons, len(dungeons))]
    
    p = k
    ans = []
    
    for dungeon in d:
        for i in range(len(dungeon)):
            if p < dungeon[i][0]:
                break
            else:
                p -= dungeon[i][1]
                answer += 1
        ans.append(answer)
        answer = 0
        p = k
    return max(ans)