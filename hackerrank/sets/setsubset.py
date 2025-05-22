test_case = int(input())
for _ in range(test_case):
    n = int(input())
    set_a = set(map(int,input().split()))
    m = int(input())
    set_b = set(map(int,input().split()))
    
    if set_a.issubset(set_b):
        print('True')
        
    else:
        print('False')