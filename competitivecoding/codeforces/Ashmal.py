#initial approach
t=int(input())
for i in range(t):
    n= int(input())
    string=[]
    lst=list(map(str,input().split()))
    for i in range(len(lst)):
        fsum=lst[i]+lst[i+1]
        bsum=lst[i+1]+lst[i]
        if fsum<bsum:
            string.append(fsum)
        else:
            string.append(bsum)

    print("".join(string))


#intermediate approach

from functools import cmp_to_key

def cmp(a,b):
    if a+b < b+a:
        return -1
    elif a+b > b+a:
        return +1
    else:
        return 0

t=int(input())
for i in range(t):
    lst=lst(map(str,input().split()))
    lst.sort(key=cmp_to_key(cmp))
    print("".join(lst))
    



#final answer   
t=int(input())
for i in range(t):
    n=int(input())
    string=""
    lst=list(map(str,input().split()))
    for i in range(len(lst)):
        if string+lst[i]<lst[i]+string:
            string=string+lst[i]
        else:
            string=lst[i]+string
    print(string)
    

