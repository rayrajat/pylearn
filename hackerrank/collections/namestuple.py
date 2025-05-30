from collections import namedtuple

n = int(input())
columns = input().split()  # read header dynamically
Student = namedtuple('Student', columns)

total_marks = 0

for _ in range(n):
    data = input().split()
    student = Student(*data)
    total_marks += int(student.MARKS)  # access MARKS by name

print(f"{total_marks / n:.2f}")
