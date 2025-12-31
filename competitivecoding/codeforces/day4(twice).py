t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = {}
    #This creates an empty dictionary

    #It will store:

    #key → the number from the array

    #value → how many times it appears

    #Example later: {1: 2, 2: 3}
    for x in arr:
        #Loop through each element in the array
        #arr = [1, 2, 1, 2, 2]
        #Then x will be:
        #1 → 2 → 1 → 2 → 2


        freq[x] = freq.get(x, 0) + 1

        #This line does three things at once:

        #🔸 freq.get(x, 0)

        #If x is already in the dictionary → return its value
        #If x is NOT in the dictionary → return 0

        #So:

        #First time you see 1 → freq.get(1, 0) = 0

        #Next time you see 1 → freq.get(1, 0) = 1

        #🔸 + 1
        #Increase the count by 1

        #🔸 Assign back to freq[x]
        #Store the updated count
        #📌 After this loop finishes

    #arr = [1, 2, 1, 2, 2]
    #freq becomes:
    #{
        #1: 2,
        #2: 3
    #}



    score = 0
   # Initialize score for this test case
    for count in freq.values():
        # Loop through only the counts

        # From the dictionary above:
        # count = 2, then 3

        score += count // 2
    #🔸 Why count // 2?

    #Each pair needs 2 equal elements

    #Integer division // tells us how many pairs we can make

#Examples:

#count	count // 2	explanation
#1	0	not enough for a pair
#2	1	one pair
#3	1	one pair, one leftover
#4	2	two pairs
#📌 Continuing the example
#freq = {1: 2, 2: 3}


#For 1: 2 // 2 = 1
    #For 2: 3 // 2 = 1

#score = 1 + 1 = 2

    print(score)

#✅ Final meaning in plain English

#Count how many times each number appears.
#From each number, form as many pairs as possible.
#Add all those pairs together.
