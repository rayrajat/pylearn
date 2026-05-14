### print pattern 5

""" ******
    *****
    ****
    ***
    **
    * """

n = int(input("Enter the number of rows: "))
for i in range(1,n):
    for j in range(i,n):
        print("*",end=" ")
    print("\n")