class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case: first row
        a = 6  # Type ABC
        b = 6  # Type ABA
        
        for _ in range(1, n):
            new_a = (3 * a + 2 * b) % MOD
            new_b = (2 * a + 2 * b) % MOD
            a, b = new_a, new_b
        
        return (a + b) % MOD


