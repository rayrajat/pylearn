t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # Maximum average subarray is just the maximum element
    print(max(arr))


#✅ Key Insight

#For any array, the maximum possible average of a subarray is simply the maximum element of the array.

#Why?

#The average of a subarray is at most the largest number in it (all terms ≤ max).

#You can always choose the subarray consisting of just that maximum element → average = that element.

#So the correct answer for each test case is:print(max(arr))