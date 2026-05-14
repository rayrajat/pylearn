t = int(input())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))

    distinct = set(arr)
    cur = len(distinct)

    # keep adding cur until cur is already in the set
    while cur not in distinct:
        distinct.add(cur)
        cur = len(distinct)

    print(cur)
