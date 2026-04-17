def discount(price, dis_per):
    return int(price * (1 - dis_per / 100))
    
    
def solution(price):
    answer = 0
    dis_per_low = 5
    dis_per_mid = 10
    dis_per_high = 20
    
    if price < 100000:
        answer = price
    elif price < 300000:
        answer = discount(price, dis_per_low)
    elif price < 500000:
        answer = discount(price, dis_per_mid)
    else:
        answer = discount(price, dis_per_high)
    return answer