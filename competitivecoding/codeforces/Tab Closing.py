t=int(input())
for _ in range(t):
    arr=list(map(int,input().split()))
    if arr[1]*arr[2]<=arr[0] or arr[1]>=arr[0]:
        print("1")
    else:
        print("2")

#https://chatgpt.com/c/6954e8b0-17e4-8322-8bc2-4e318737534c