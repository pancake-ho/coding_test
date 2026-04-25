def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)
        

def solution(n):
    answer = 0
    for i in range(1, 9):
        if n == 3628800:
            answer = 10
            break
        if fact(i) <= n < fact(i+1):
            answer = i
    return answer