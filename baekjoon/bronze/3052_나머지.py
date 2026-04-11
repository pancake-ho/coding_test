answer = []
answer_num = 0

for i in range(10):
    num = int(input())
    if num%42 not in answer:
        answer.append(num%42)
        answer_num += 1
    
print(answer_num)