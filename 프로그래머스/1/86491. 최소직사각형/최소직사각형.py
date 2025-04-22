def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
    
    max_width = max(sizes[i][0] for i in range(len(sizes)))
    max_height = max(sizes[i][1] for i in range(len(sizes)))
    
    
    
    
    answer = max_width * max_height
    return answer