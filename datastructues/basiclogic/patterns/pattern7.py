## print pattern 7

"""   *
     * *
    * * *
   * * * *  """


for i in range(1,6):

    # spaces
    for j in range(5-i):
        print(" ", end="")

    # stars
    for k in range(2*i-1):
        print("*", end="")

    print()