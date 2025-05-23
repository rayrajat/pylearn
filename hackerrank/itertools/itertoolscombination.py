from itertools import combinations

string,k = input().split()
for i in range(1,int(k)+1):
    for j in list(combinations(sorted(string),i)):
        print("".join(j))


'''This imports the combinations function from the itertools module.

combinations generates all possible combinations of a given length without considering order (unlike permutations).'''



#string,k = input().split()

'''akes input from the user, splits it by spaces into two parts.

Assigns the first part to string (a string of characters).

Assigns the second part to k (a string representing a number).

For example, input:
HACK 2

Here, string = "HACK" and k = "2".'''
#for i in range(1,int(k)+1):
 #'''Converts k to an integer.

 # Creates a loop variable i that runs from 1 to k inclusive.

# This means it will generate combinations of length 1, 2, ..., up to k.'''




    #for j in list(combinations(sorted(string),i)):
   
   
 #'''First, sorted(string) sorts the characters in the string in alphabetical order.

#For example, "HACK" sorted becomes ['A', 'C', 'H', 'K'].

#combinations(sorted(string), i) generates all combinations of length i from the sorted characters.

#list(...) converts the combinations generator into a list of tuples.

#The inner loop iterates over each combination tuple j.'''

#python
#Copy
#Edit'''

        #print("".join(j))

#"".join(j) converts the tuple j (like ('A', 'C')) into a string "AC".

#print(...) outputs this string.



