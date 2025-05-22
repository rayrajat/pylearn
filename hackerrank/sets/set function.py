n = int(input())
s = set(map(int, input().split()))
#n = int(input())
#set_a = list(set(list(map(int,input().split()))))
m = int(input())

for _ in range(m):
    command, *line = input().split()
    values = list(map(int, line))

    match command:
        case 'remove':
            s.remove(values[0])
        case 'pop':
            s.pop()
        case 'discard':
            s.discard(values[0])
print(sum(s))