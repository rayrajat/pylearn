## print pattern 11

"""  1
     0 1
     1 0 1
     0 1 0 1
     1 0 1 0 1 """

n= int(input("Enter the number of rows: "))
for i in range(1,n):

    for j in range(1,i+1):

        print((i+j+1)%2, end=" ")

    print()


## if starting with 0 then print (i+j)%2