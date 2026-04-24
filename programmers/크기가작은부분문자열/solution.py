def solution(t, p):
    answer = 0
    nums_list = []
    
    for i in range(len(t)):
        nums_list.append(t[i: i+len(p)])
    nums_list = [x for x in nums_list if len(x) == len(p)]
    
    for num in nums_list:
        if num <= p:
            answer += 1
    return answer