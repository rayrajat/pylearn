from itertools import groupby
s = input()
for i,j in groupby(s):
    print(tuple([len(list(j)),int(i)]),end=" ")


#from itertools import groupby

'''This imports the groupby() function from the itertools module.

groupby() groups consecutive identical items in an iterable.'''

#s = input()

'''Takes a string input from the user.
Example input: 1222311'''


#for i,j in groupby(s):
'''This loop uses groupby() to group consecutive repeating characters in the input string s.

i is the character being grouped (as a string).

j is an iterator over the group of consecutive matching characters.'''

    #print(tuple([len(list(j)),int(i)]),end=" ")

'''list(j) converts the group iterator j into a list of repeated characters (e.g., ['2', '2', '2']).

len(list(j)) gives the count of consecutive repetitions.

int(i) converts the character (which is a string) into an integer.

tuple([len(...), int(...)]) creates a tuple: (count, digit).

end=" " keeps the output on the same line with spaces in between.'''


#example ;

#Step-by-step grouping:

#'1' → occurs once → (1, 1)

#'2' → occurs 3 times → (3, 2)

#'3' → occurs once → (1, 3)

#'1' → occurs twice → (2, 1)

#Output:

#scss
#Copy
#Edit
#(1, 1) (3, 2) (1, 3) (2, 1)



