class Solution:
    def minTime(self, rank, n):
        def canCompleteIn(time):
            total = 0
            for r in rank:
                # Using quadratic formula is faster & cleaner
                # r*x*(x+1)/2 <= time
                # x^2 + x - 2*time/r <= 0
                disc = 1 + 8 * time // r
                x = int((-1 + disc ** 0.5) / 2)
                total += x
                if total >= n:
                    return True
            return total >= n
        
        lo, hi = 0, 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            if canCompleteIn(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo