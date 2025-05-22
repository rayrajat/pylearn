set_a = set(map(int,input().split()))

n = int(input())

print(all([set_a.issuperset(set(map(int,input().split())))for _ in range(n)]))


'''The Python all() function returns true if all the elements of a given iterable (List, Dictionary, Tuple, set, etc.) are True otherwise it returns False. It also returns True if the iterable object is empty. Sometimes while working on some code if we want to ensure that user has not entered a False value then we use the all() function.

Python all() Function in Python

Syntax: all( iterable )


Iterable: It is an iterable object such as a dictionary,tuple,list,set,etc.

Returns: boolean'''


