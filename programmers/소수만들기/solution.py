def prime_num(num):
    answer = 0
    
    for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                if i * i == num:
                    answer += 1
                else:
                    answer += 2
    return answer

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if prime_num(nums[i]+nums[j]+nums[k]) == 2:
                    answer += 1

    return answer