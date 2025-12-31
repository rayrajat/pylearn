class Solution:
    def kthSmallest(self, mat, k):
        if not mat or not mat[0]:
            return -1
            
        n = len(mat)
        m = len(mat[0])
        
        # Binary search on the value range
        left = mat[0][0]           # smallest element
        right = mat[n-1][m-1]      # largest element
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Count how many elements ≤ mid
            count = self.countLessEqual(mat, mid)
            
            if count < k:
                left = mid + 1
            else:
                right = mid
                
        return left
    
    def countLessEqual(self, mat, target):
        n = len(mat)
        m = len(mat[0])
        count = 0
        row = n - 1
        col = 0
        
        while row >= 0 and col < m:
            if mat[row][col] <= target:
                count += row + 1      # all elements in this column from 0 to row are ≤ target
                col += 1              # move right
            else:
                row -= 1              # move up
                
        return count
