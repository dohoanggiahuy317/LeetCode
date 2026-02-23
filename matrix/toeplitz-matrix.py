class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for j in range(n):
            for diff in range(m):
                if diff + j < n and not matrix[diff][diff + j] == matrix[0][j]:
                    return False
        
        return True