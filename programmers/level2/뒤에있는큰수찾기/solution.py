def solution(numbers):
    answer = [-1] * len(numbers)
    num_stack = []
    
    for i in range(len(numbers)):
        while num_stack and numbers[num_stack[-1]] < numbers[i]:
            idx = num_stack.pop()
            answer[idx] = numbers[i]
        
        num_stack.append(i)
        
    return answer