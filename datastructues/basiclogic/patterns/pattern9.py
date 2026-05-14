## print pattern 9
"""
    *
   * *
  * * *
 * * * *
 * * * *
  * * *
   * *
    * """


# Upper pyramid
for i in range(1,6):

    # spaces
    for j in range(5-i):
        print(" ", end="")

    # stars
    for k in range(2*i-1):
        print("*", end="")

    print()


# Lower inverted pyramid
for i in range(4,0,-1):

    # spaces
    for j in range(5-i):
        print(" ", end="")

    # stars
    for k in range(2*i-1):
        print("*", end="")

    print()