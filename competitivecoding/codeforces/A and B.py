def min_swaps_group(s, ch):
    pos = [i for i, c in enumerate(s) if c == ch]
    k = len(pos)
    
    if k == 0:
        return 0
    
    adjusted = [pos[i] - i for i in range(k)]
    adjusted.sort()
    
    median = adjusted[k // 2]
    cost = sum(abs(x - median) for x in adjusted)
    
    return cost


def solve(s):
    return min(
        min_swaps_group(s, 'a'),
        min_swaps_group(s, 'b')
    )

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s=input().strip()
        print(solve(s))


# Codeforces Problem A and B

import sys
input = sys.stdin.readline

def cost_to_group(pos):
    k = len(pos)
    if k <= 1:
        return 0

    mid = k // 2
    median = pos[mid] - mid

    cost = 0
    for i in range(k):
        cost += abs((pos[i] - i) - median)

    return cost

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()

        pos_a = []
        pos_b = []

        for i, c in enumerate(s):
            if c == 'a':
                pos_a.append(i)
            else:
                pos_b.append(i)

        ans = min(cost_to_group(pos_a), cost_to_group(pos_b))
        print(ans)

if __name__ == "__main__":
    solve()
