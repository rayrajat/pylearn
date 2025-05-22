n = int(input())

set_a = set(map(int,input().split()))

n = int(input())

for _ in range(n):
    command, *line = input().split()
    values = list(map(int, line))
    set_b = set(map(int,input().split()))
    
    match command:
        case 'intersection_update':
            set_a.intersection_update(set_b)
        case 'update':
            set_a.update(set_b)
        case 'symmetric_difference_update':
            set_a.symmetric_difference_update(set_b)
        case 'difference_update':
            set_a.difference_update(set_b)
            
print(sum(set_a))