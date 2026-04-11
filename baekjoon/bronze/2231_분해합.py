N = int(input())
answer = 0

for i in range(1, N+1):
    nums = list(map(int, str(i)))
    num_sum = sum(nums) + i
    if num_sum == N:
        answer = i
        break

print(answer)