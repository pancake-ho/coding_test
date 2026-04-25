def solution(k, tangerine):
    answer = 0
    tangerines = {}
    
    for fruit in tangerine:
        if fruit not in tangerines:
            tangerines[fruit] = 1
        else:
            tangerines[fruit] += 1
    
    sorted_tangerines = dict(sorted(tangerines.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_tangerines.items():
        if k - value <= 0:
            answer += 1
            break
        else:
            k -= value
            answer += 1
    return answer