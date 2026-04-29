def solution(array, n):
    answer = 0
    array.sort()
    diff = 100
    for num in array:
        if diff > abs(num - n):
            diff = abs(num - n)
            answer = num
    print(diff)
    return answer