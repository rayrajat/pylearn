class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_abs_sum = 0
        neg_count = 0
        min_abs_val = float('inf')
        
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                abs_val = abs(val)
                total_abs_sum += abs_val
                min_abs_val = min(min_abs_val, abs_val)
        
        # If odd number of negatives, one must remain negative
        if neg_count % 2 == 1:
            return total_abs_sum - 2 * min_abs_val
        return total_abs_sum
