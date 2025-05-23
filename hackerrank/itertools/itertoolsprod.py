from itertools import product

a = map(int,input().split())
b = map(int,input().split())

for i in product(a,b):
    print(i,end=" ")


#The itertools module in Python is a standard library module that provides a collection of fast, memory-efficient tools for working with iterators.
#These tools are useful for creating and using iterators for efficient looping, especially when dealing with large datasets or infinite sequences.

