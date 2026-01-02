#my solution
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int: # type: ignore
        count=0
        for i in nums:
            for j in nums:
                if nums[i]==nums[j]:
                    count=count+1
            if count>1:
                return nums[i]
            
#actual solution
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int: # type: ignore
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)