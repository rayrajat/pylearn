class Solution:
    def kthElement(self, a, b, k):
        # code here
        new_arr = a+b
        new_arr.sort()
        return new_arr[k-1]