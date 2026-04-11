N = int(input())
input_list = list(map(int, input().split()))

min = 1e9
max = -1e9

for i in range(N):
    if input_list[i] > max:
        max = input_list[i]

    if input_list[i] < min:
        min = input_list[i]

print(min, max)