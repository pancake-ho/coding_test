def convert(n):
    digits = "01"
    answer = 0
    
    if n == 0:
        return "0"
    
    result = []
    
    while n > 0:
        result.append(digits[n%2])
        n = n // 2
    
    return result.count('1')

def solution(n):
    answer = n + 1
    print(convert(n))
    
    while convert(n) != convert(answer):
        answer += 1
    return answer