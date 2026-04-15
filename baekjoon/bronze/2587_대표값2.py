nums_list = []
nums_sum = 0

for i in range(5):
    num = int(input())
    nums_list.append(num)

nums_list.sort()

for i in range(5):
    nums_sum += nums_list[i]

print(int(nums_sum / 5))
print(nums_list[2])