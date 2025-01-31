class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        zeroth_row = set()
        zeroth_col = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zeroth_row.add(i)
                    zeroth_col.add(j)
        for i in range(r):
            if i in zeroth_row:
                matrix[i] = [0] * c

        for j in range(c):
            if j in zeroth_col:
                for i in range(r):
                    matrix[i][j] = 0

# Time Complexity: O(m*n)
# Space Complexity: O(m+n)
# Approach 2
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        zeroth_row = False
        for i in range(r):
            if matrix[i][0] == 0:
                zeroth_row = True
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zeroth_row:
            for i in range(r):
                matrix[i][0] = 0
    '''             
# Time Complexity: O(m*n)
# Space Complexity: O(1)