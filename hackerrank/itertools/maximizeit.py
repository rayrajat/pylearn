from itertools import combinations
N = int(input())
string=input().split()
k=int(input())
combination = list(combinations(string, k))
count = 0
for i in combination:
    if 'a' in i:
        count += 1


probability=count/len(combination)
print(f'{probability:.3f}')

# explanation

'''K , M = list(map(int,input().split()))
Reads two integers from input:

K: Number of lists to read

M: The modulo value used in the final sum

python
Copy
Edit
List = [list(map(int, input().split()))[1:] for i in range(K)]
Reads K lines of input, each containing:

First number: the number of elements in the list (this value is ignored with [1:])

Remaining numbers: the list elements

Collects all the lists into a master list called List.

Example input:

yaml
Copy
Edit
3 1000
2 5 4
2 7 8
2 9 10
Then, List = [[5, 4], [7, 8], [9, 10]]

python
Copy
Edit
Possible_sum = {0}
Initializes a set that will store all possible sums (mod M) we can achieve by selecting one number from each list.

Starts with just {0} meaning we haven't added anything yet.

python
Copy
Edit
for lst in List:
    new_sum = set()
    for num in lst:
        for s in Possible_sum:
            new_sum.add((s + num**2) % M)
    Possible_sum = new_sum
This block does the core logic:

Loop Over Lists:
For each list in List:

Initialize a new set new_sum to store updated values.

Loop Over Numbers:
For each number in the current list:

Square the number (as per the problem statement).

Add this square to each value already in Possible_sum, take modulo M, and store in new_sum.

After considering all numbers from the current list, Possible_sum is updated with the newly calculated values.

This ensures that for every combination of selecting one number per list, all possible sums of squares modulo M are considered.

python
Copy
Edit
print(max(Possible_sum))
Finally, prints the maximum value possible from all these modular sums.

🔸 Example Walkthrough:
Input:

yaml
Copy
Edit
3 1000
2 5 4
2 7 8
2 9 10
Let’s simulate what happens:

Initial Possible_sum = {0}

After first list [5, 4]
5² = 25, 4² = 16

Add to 0 → new sums: 25, 16

Possible_sum = {16, 25}

After second list [7, 8]
7² = 49, 8² = 64

Add to existing sums:

16 + 49 = 65

16 + 64 = 80

25 + 49 = 74

25 + 64 = 89

Possible_sum = {65, 74, 80, 89}

After third list [9, 10]
9² = 81, 10² = 100

Add to each in Possible_sum:

e.g., 65 + 81 = 146, 65 + 100 = 165, ...

Final Possible_sum = {146, 155, 165, 173, 181, 189, 190, 199}

Final Answer:
Copy
Edit
199'''