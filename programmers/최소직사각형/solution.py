def solution(sizes):
    cand = []
    sizes.sort(key=max)
    max_value = max(map(max, sizes))
    
    for i in sizes:
        cand.append(min(i))
    answer = max(cand) * max_value
    return answer