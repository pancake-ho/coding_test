def LCM(a, b = 6):
    while True:
        if a > b:
            if a % b == 0:
                return a
        else:
            if b % a == 0:
                return b
        b += 6

def solution(n):
    answer = LCM(n, 6) // 6
    return answer