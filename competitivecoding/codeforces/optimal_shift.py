import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    # Find longest consecutive zeros in the cyclic string
    max_zero = 0
    cnt = 0

    # We’ll go through the string twice to cover the cyclic nature
    double = s + s
    for ch in double:
        if ch == '0':
            cnt += 1
            max_zero = max(max_zero, cnt)
        else:
            cnt = 0

    # But we only want sequences up to length n
    # (a stretch longer than n means all zeros, but problem guarantees >=1 one)
    if max_zero > n:
        max_zero = n

    print(max_zero)
