## print pattern 3

""" 1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5 """


n =  int(input("Enter the number of rows: "))
for i in range(1,n):
    for j in range(i):
        print(j+1,end=" ")
    print("\n")
