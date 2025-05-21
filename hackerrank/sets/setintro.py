#A set in Python is an unordered collection of unique elements. Python provides several built-in methods to perform various operations on sets.

def average(array):
    # your code goes here
    
    array = list(set(array))

    avg = sum(array)/len(array)
    return avg
    
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)