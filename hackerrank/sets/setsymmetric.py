n = int(input())
set_a = set(map(int,input().split()))
m = int(input())
set_b = set(map(int,input().split()))

set_c = set_a.symmetric_difference(set_b)
print(len(set_c))