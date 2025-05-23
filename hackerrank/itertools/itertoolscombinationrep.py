from itertools import combinations_with_replacement

string,k = input().split()

for i in list(combinations_with_replacement(sorted(string),int(k))):
    print("".join(i))