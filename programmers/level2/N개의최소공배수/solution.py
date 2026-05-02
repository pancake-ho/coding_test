def gcd(m, n):
    while n:
        m, n = n, m%n
    return m

def lcd(m, n):
    return (m * n) // gcd(m, n)

def solution(arr):
    answer = 0
    for i in range(len(arr)):
        if i == len(arr)-1:
            break
        else:
            arr[i+1] = lcd(arr[i], arr[i+1])
            answer = arr[i+1]
    return answer