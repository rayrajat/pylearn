from collections import defaultdict

# Read input sizes
n = list(map(int, input().split()))

group_a = []
group_b = []

# Read group A
for _ in range(n[0]):
    s = input()
    group_a.append(s)

# Read group B
for _ in range(n[1]):
    s = input()
    group_b.append(s)

# Store positions of words in group A
position = defaultdict(list)
for index, word in enumerate(group_a, start=1):
    position[word].append(index)

# For each word in group B, print positions or -1
for word in group_b:
    if word in position:
        print(*position[word])
    else:
        print(-1)




# defaultdict
'''The defaultdict is a dictionary-like structure provided by Python's collections module that automatically assigns a default value to a key when it is first accessed, if that key doesn't exist yet. This behavior differentiates it from a standard Python dictionary, which raises a KeyError if you try to access a non-existent key.
Key Features:
Default Value: When initializing a defaultdict, you provide a "default factory," which is a function that takes no arguments and returns the default value. This factory is called when a missing key is encountered.
No KeyError: Unlike regular dictionaries, defaultdict will not raise a KeyError when accessing a key that has not been added to the dictionary. Instead, it will use the default factory to create the key with a default value.
Subclass of dict: It inherits the properties and methods of the built-in dict class.
How it works:
When you try to access a key in a defaultdict, it first checks if the key exists.
If the key exists, it returns the corresponding value.
If the key does not exist, it calls the default factory function to create a default value. This default value is then associated with the key, and the value is returned.
Examples:
Python

from collections import defaultdict

# Using list as the default factory
my_dict = defaultdict(list)
my_dict['a'].append(1)  # No KeyError, 'a' is created with an empty list
print(my_dict) # Output: defaultdict(<class 'list'>, {'a': [1]})

# Using int as the default factory
count_dict = defaultdict(int)
count_dict['apple'] += 1 # No KeyError, 'apple' is created with a default value of 0
print(count_dict) # Output: defaultdict(<class 'int'>, {'apple': 1})
Use Cases:
Counting occurrences: Useful for counting elements in a list or other iterable without having to check if a key exists.
Grouping items: Can be used to group items based on a key.
Avoiding KeyError: Simplifies code by eliminating the need to check for key existence before accessing or modifying values.
Advantages:
Code Clarity: Reduces boilerplate code by eliminating the need for if key in dict checks.
Efficiency: Can be slightly faster than using a regular dictionary with key checks.
In summary, defaultdict is a useful tool for simplifying dictionary operations when dealing with missing keys by automatically creating keys with default values, which makes your code cleaner and more efficient.'''






