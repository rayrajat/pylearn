number = int(input())
for i in range(number):
    edges = list(map(int, input().split()))
    if edges[0]== edges[1]== edges[2] == edges[3]:
        print("YES")
    else:
        print("NO")

#codeforces question 2167A SQUARE? WE given four edges of a quadrilateral,
# we have to check whether it is a square or not. 
# A square has all four sides equal.

# logic: just if all four input numbers are equal print yes else no 