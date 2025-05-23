from itertools import combinations

n = int(input())
string = input().split()
k = int(input())

combination = list(combinations(string,k))
count = 0
for i in combination:
    if 'a' in i:
        count += 1
    
probablity = count/len(combination)

print(f'{probablity:.3f}')


# explanation

'''from itertools import combinations
This imports the combinations function from the itertools module.

It is used to generate all possible unordered combinations of a specified length from a sequence.

python
Copy
Edit
N = int(input())
Reads an integer N which represents the total number of elements in the list that will be entered next.

python
Copy
Edit
string = input().split()
Reads a line of input and splits it into a list of strings.

This list should contain exactly N elements.

Example:
Input: a b c d
Output: ['a', 'b', 'c', 'd']

python
Copy
Edit
k = int(input())
Reads an integer k, the size of each combination to generate.

python
Copy
Edit
combination = list(combinations(string, k))
Generates all possible combinations of length k from the list string.

Stores these combinations in a list.

python
Copy
Edit
count = 0
for i in combination:
    if 'a' in i:
        count += 1
Initializes count to 0.

Iterates over each combination i.

If 'a' is present in the combination, increments count by 1.

So count becomes the number of combinations that include the letter 'a'.

python
Copy
Edit
probability = count / len(combination)
Calculates the probability that a randomly selected combination includes 'a'.

This is simply the number of "favorable" combinations (those that include 'a') divided by the total number of combinations.

python
Copy
Edit
print(f'{probability:.3f}')
Prints the probability, rounded to 3 decimal places.'''

