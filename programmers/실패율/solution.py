def solution(N, stages):
    answer = []
    counts = {}
    probs = {}
    
    for i in range(1, N+1):
        counts[i] = 0
    
    for stage in stages:
        if stage <= N:
            counts[stage] += 1
    
    total_users = len(stages)

    for stage in range(1, N+1):
        if total_users == 0:
            probs[stage] = 0
        else:
            probs[stage] = counts[stage] / total_users
            total_users -= counts[stage]
            
    sorted_stages = sorted(probs.items(), key=lambda x: x[1], reverse=True)
    for stage, prob in sorted_stages:
        answer.append(stage)
    return answer