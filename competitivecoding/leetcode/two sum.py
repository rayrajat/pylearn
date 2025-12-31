from typing import List
class Solution:
    def twosum(self, nums: list[int],target: int) -> list[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]





# Example usage:sol = Solution()
print(Solution.twosum([2,7,11,15],9))
