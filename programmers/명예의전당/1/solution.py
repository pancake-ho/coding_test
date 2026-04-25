def solution(k, score):
    cand = []
    answer = []
    for i in range(len(score)):
        if len(cand) < k:
            cand.append(score[i])
        else:
            if score[i] < min(cand):
                pass
            else:
                cand.remove(min(cand))
                cand.append(score[i])
        answer.append(min(cand))
    return answer