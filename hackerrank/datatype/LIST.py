N = []

n = int(input())

for _ in range(n):
    command, *line = input().split()
    values = list(map(int, line))

    match command:
        case 'insert':
            N.insert(values[0], values[1])
        case 'append':
            N.append(values[0])
        case 'remove':
            N.remove(values[0])
        case 'pop':
            N.pop()
        case 'sort':
            N.sort()
        case 'reverse':
            N.reverse()
        case 'print':
            print(N)


    

    
