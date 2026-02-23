class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[0][0] == matrix[i][i] for i in range(min(len(matrix), len(matrix[0]))))