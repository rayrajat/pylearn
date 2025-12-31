class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: # type: ignore
        num3=nums1+nums2
        num3.sort()
        if len(num3)%2!=0:
            median_odd = num3[(len(num3)-1)//2]
            return median_odd
        else:
            middle = num3[(len(num3)//2) - 1 : (len(num3)//2) + 1]
            median_even=sum(middle)/2
            return median_even