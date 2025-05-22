import sys

#This line imports the sys module, which allows you to access lower-level system 
# operations — including fast input reading with sys.stdin.read().



# Fast input reading
input = sys.stdin.read

#This replaces the standard input() function with sys.stdin.read, allowing you to read all input at once (as one big string). 
#This is much faster than calling input() repeatedly, especially useful for large inputs in competitive programming.


data = input().split()

#input() now reads the entire input as one string.

#.split() splits that string into a list of words or numbers (as strings), 
# using whitespace (spaces, tabs, or newlines) as separators.

# First N elements are the list

n = int(data[0])  # size of List

m = int(data[1])  # not always needed

List = list(map(int, data[2:2+n]))

#data[2:2+n] slices the input list to get the next n values.

#map(int, ...) converts each string to an integer.

#list(...) turns the mapped values into a list.

#📦 Result: List now contains the main list of integers we're evaluating for happiness.

set_a = set(map(int, data[2+n:2+n+m]))

'''This grabs the next m numbers after the main list, which belong to set_a.

Converts them to integers.

Wraps them in a set for fast O(1) lookup during happiness checking.

📦 Result: set_a contains the elements that increase happiness.'''

set_b = set(map(int, data[2+n+m:]))


'''This gets the remaining m numbers in the input after set_a, which are for set_b.

Converts them to integers and stores in a set.

📦 Result: set_b contains the elements that decrease happiness.'''

happiness = 0

for i in List:
    if  i in set_a:
        happiness+=1
    elif i in set_b:
        happiness-=1

print(happiness)
