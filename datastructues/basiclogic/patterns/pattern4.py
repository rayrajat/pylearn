### print pattern 4
""" 1
    22
    333
    4444
    55555"""


n =  int(input("Enter the number of rows: "))   
for i in range(1,n):
    for j in range(i):
        print(i,end=" ")
    print("\n")