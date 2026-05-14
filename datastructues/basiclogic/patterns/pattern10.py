### print pattern 10

""" *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    * """

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()
    
    
for i in range(n-2,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()