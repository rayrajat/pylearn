#1 st attempt
test_case = int(input())
arr = list(map(int,input().split()))
arr.sort()

x = int(input())
num = []

for i in range(len(arr) - 1):
    mid = (arr[i] + arr[i + 1]) / 2
    if mid.is_integer():
        num.append(int(mid))

# check if x lies between min and max of num
if num and min(num) <= x <= max(num):
    print("YES")
else:
    print("NO")

#2 attempt

test_cases=int(input())
for i in range(test_cases):
    n=int(input())
    arr=list(map(int,input().split()))
    x=int(input())
    if min(arr)<=x<=max(arr):
        print("YES")
    else:
        print("NO")



    

     