def solution(s):
    answer = []
    s_arr = {}
    
    for i in range(len(s)):
        name = s[i]
        if name in s_arr:
            answer.append(i - s_arr[name])
        else:
            answer.append(-1)
        
        s_arr[name] = i
            
    print(s_arr)
    return answer