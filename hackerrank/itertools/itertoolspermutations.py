from itertools import permutations
''''This imports the permutations function from the itertools module.

permutations generates all possible ordered arrangements (permutations) of elements from a sequence.'''




string,k = input().split()

'''his takes a single input line from the user and splits it by whitespace into two parts.

The first part is assigned to string (a string of characters).

The second part is assigned to k (a string representing a number).

For example, if the user inputs:
ABC 2
then string = 'ABC' and k = '2'.

python
Copy
Edit'''



for i in sorted(list(permutations(string,int(k)))):



    print("".join(i))
'''int(k) converts the string k to an integer.

permutations(string, int(k)) generates all possible permutations of length k from the characters in string.

For example, if string = "ABC" and k = 2, it generates: ('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B').

list(...) converts the permutations generator into a list.

sorted(...) sorts this list of tuples lexicographically (dictionary order).

The for loop iterates over each sorted permutation tuple, assigning it to i in each iteration.'''


    #print("".join(i))
     

# ().join(i) converts the tuple i (like ('A', 'B')) into a string ("AB").

#print(...) outputs this string to the console.'''


    
