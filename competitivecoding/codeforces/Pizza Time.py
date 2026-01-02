"""test_case=int(input())
for _ in range(test_case):
    n=int(input())
    division = n//3
    m1=division
    m2=(n-division)//2
    m3=n-(m1+m2)
    hao=m1
    while m3>=2:
        div=m3//3
        n1=div
        n2=(m3-div)//2
        n3=m3-(n1+n2)
    
        hao=hao+n1
        m3=n3
    print(hao)"""



#actual solution

t = int(input())
for _ in range(t):
    n = int(input())
    print((n - 1) // 2)

