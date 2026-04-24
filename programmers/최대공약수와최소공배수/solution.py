def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def solution(n, m):
    answer = [gcd(n, m), (n*m)/gcd(n,m)]
    return answer