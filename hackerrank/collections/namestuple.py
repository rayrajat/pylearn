from collections import namedtuple
n = int(input())
Student = namedtuple('Student',['ID','MARKS','NAME','CLASS'])
students = []
for i in range(n):
    data = input().split()
    student = Student(ID=data[0],MARKS=data[1],NAME=data[2],CLASS=data[3])
    students.append(student)

total_marks = sum(s.MARKS for s in students)
print(f"average_marks:{total_marks / n:.2f}")



