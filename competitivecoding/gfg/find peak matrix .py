#Given a 2D matrix mat[][], identify any peak element within the matrix.

#An element is considered a peak if it is greater than or equal to its four immediate neighbors: top, bottom, left, and right. For corner and edge elements, any missing neighbors are treated as having a value of negative infinity.

#Note: A peak element is not necessarily the global maximum, it only needs to satisfy the condition relative to its adjacent elements. Multiple peak elements may exist, return any one of them.
#Note that the driver code will print true if you return the correct position of peak element, else it will print false.

#Constraint:
#1 ≤ n × m ≤ 106
#-106 ≤ mat[i][j] ≤ 106


#solution

class Solution:
    def findPeakGrid(self, mat):
        if not mat or not mat[0]:
            return [-1, -1]
            
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(m):
                curr = mat[i][j]
                is_peak = True
                
                # top
                if i > 0 and mat[i-1][j] > curr:
                    is_peak = False
                # bottom
                if i < n-1 and mat[i+1][j] > curr:
                    is_peak = False
                # left
                if j > 0 and mat[i][j-1] > curr:
                    is_peak = False
                # right
                if j < m-1 and mat[i][j+1] > curr:
                    is_peak = False
                    
                if is_peak:
                    return [i, j]
                    
        return [-1, -1]  # though problem guarantees at least one peak exists