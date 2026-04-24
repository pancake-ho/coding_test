def convert(n):
    digits = "012"
    
    if n == 0:
        return "0"

    result = []
    
    while n > 0:
        result.append(digits[n%3])
        n = n // 3
    
    return "".join(result)

def reconvert(n):
    result = 0
    
    for i, ch in enumerate(reversed(n)):
        result += int(ch) * (3 ** i)
    return result

def solution(n):
    answer = 0
    
    n = convert(n)
    answer = reconvert(n)
    
    return answer