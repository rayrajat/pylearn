#solution1
t = int(input())
for _ in range(t):
    input()                     
    s = input().strip()
    target = input().strip()
    
    if sorted(s) == sorted(target):
        print("YES")
    else:
        print("NO")

#solution 2
for _ in range(int(input())):
    input()                           # skip n m
    print("YES" if sorted(input().strip()) == sorted(input().strip()) else "NO")

# solution 3
for _ in range(int(input())):input();print("YES"if sorted(input().strip())==sorted(input().strip())else"NO")


#solution 4 worth it and actual solution 
import sys

input = sys.stdin.read
data = input().split()

index = 0
q = int(data[index])
index += 1

for _ in range(q):
    # skip n (we don't need it)
    index += 1
    s = data[index]
    index += 1
    t = data[index]
    index += 1
    
    if sorted(s) == sorted(t):
        print("YES")
    else:
        print("NO")

        
#problem my description
# Given two strings s and target of equal length, determine if s can be rearranged to form target.
# For each test case, output "YES" if s can be rearranged to form target, otherwise output "NO".

#logic
#it can be solved if check if both two strings have same characters with same frequeency easy!
