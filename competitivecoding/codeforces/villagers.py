import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    g = list(map(int, input().split()))
    
    g.sort()
    
    ans = 0
    # take every second element from the largest
    for i in range(n - 1, -1, -2):
        ans += g[i]
    
    print(ans)
