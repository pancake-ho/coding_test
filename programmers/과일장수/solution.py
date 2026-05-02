def solution(k, m, score):
    answer = 0
    box = []
    
    score.sort(reverse=True)

    for i in range(len(score)):
        box.append(score[i])
        if len(box) == m:
            answer += m * min(box)
            box = []
     
    return answer