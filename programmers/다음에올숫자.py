def solution(common):
    answer = 0
    common_d = common[1] - common[0]
    common_d_test = common[2] - common[1]

    if (common_d == common_d_test):
        answer = common[-1] + common_d
    else:
        common_r = common[1] // common[0]
        answer = common[-1] * common_r
    return answer