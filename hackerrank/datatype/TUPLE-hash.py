#https://www.geeksforgeeks.org/python-hash-method/

'''In Python 3.3 and above, the hash() function is randomized by default across sessions.

This means that the hash of the same object (e.g. a tuple) may differ every time you run the program.

This behavior is a security feature (enabled via PYTHONHASHSEED=random).

In contrast, Python 2 or Python 3 with a fixed PYTHONHASHSEED gives consistent hash values.'''


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))