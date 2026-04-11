student = []
student_id = []

for i in range(28):
    s = int(input())
    student.append(s)
    student_id.append(i)

student.sort()
student_id.sort()

for i in range(1, 31):
    if i not in student:
        print(i)