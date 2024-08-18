class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        # find the rows and columns with 0
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # second loop to find any cells in same rows or columns
        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                if i in rows or j in cols:
                    matrix[i][j] = 0

        return 