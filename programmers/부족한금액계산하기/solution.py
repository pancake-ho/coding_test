def solution(price, money, count):
    answer = 0
    price_sum = 0
    
    for i in range(count):
        price_sum += price * (i+1)
    
    if money <= price_sum:
        answer = price_sum - money
    else:
        answer = 0
    return answer