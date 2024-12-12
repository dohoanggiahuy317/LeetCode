class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        for i in range(n//2):
            for j in range(i, n-i-1):
                t1 = matrix[i][j]
                t2 = matrix[j][n-1-i]
                t3 = matrix[n-1-i][n-1-j]
                t4 = matrix[n-1-j][i]                 
                matrix[i][j] = t4
                matrix[j][n-1-i] = t1
                matrix[n-1-i][n-1-j] = t2
                matrix[n-1-j][i] = t3
                
                
                
                