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