t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    target = s[-1]
    ans = sum(1 for i in range(n - 1) if s[i] != target)
    print(ans)
