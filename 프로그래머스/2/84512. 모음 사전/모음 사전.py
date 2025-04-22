from itertools import product
def solution(word):
    wordList = []
    for i in range(1, 6):
        for p in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            wordList.append("".join(p))
    
    order = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    s = sorted(wordList, key=lambda word: [order[c] for c in word])
    
    answer = s.index(word) + 1
    return answer