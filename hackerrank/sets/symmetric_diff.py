#If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) by default. To specify that comma is the delimiter, use string.split(','). For this challenge, and in general on HackerRank, space will be the delimiter.
'''The symmetric_difference() method returns a new set that contains elements either in one set or the other, but not in both.
It's like subtracting the intersection from the union.'''

#set1.symmetric_difference(set2)
#You can also use the caret (^) operator:
#set1 ^ set2



M = int(input())
set_m = set(list(map(int,input().split())))
N = int(input())
set_n = set(list(map(int,input().split())))

diference = set_m.symmetric_difference(set_n)

for diff in sorted(diference):
    print(diff)