def solution(s, n):
    alpha_small = "abcdefghijklmnopqrstuvwxyz"
    alpha_large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    answer = ''
    for alpha in s:
        if alpha == ' ':
            answer += " "
        elif alpha.islower():
            if (alpha_small.index(alpha) + n) >= len(alpha_small):
                idx = alpha_small.index(alpha) + n - len(alpha_small)
            else:
                idx = alpha_small.index(alpha) + n
            answer += alpha_small[idx]
        else:
            if (alpha_large.index(alpha) + n) >= len(alpha_large):
                idx = alpha_large.index(alpha) + n - len(alpha_large)
            else:
                idx = alpha_large.index(alpha) + n
            answer += alpha_large[idx]
    return answer