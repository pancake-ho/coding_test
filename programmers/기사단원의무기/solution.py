def num_div(number):
    answer = 0
    
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            if i * i == number:
                answer += 1
            else:
                answer += 2
    
    return answer

def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        if num_div(num) <= limit:
            answer += num_div(num)
        else:
            answer += power
    return answer