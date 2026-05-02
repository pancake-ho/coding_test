def solution(numbers, target):
    result = []
    
    def dfs(idx, total):
        if idx == len(numbers):
            result.append(total)
            return
        
        dfs(idx+1, total + numbers[idx])
        dfs(idx-1, total - numbers[idx])
    
    dfs(0, 0)
    
    return result.count(target)