class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    
        m, n = len(mat), len(mat[0])
        zigzag = []

        for diag in range(m + n - 1):
            for i in range(diag + 1):
                
                if diag % 2 == 0:
                    i = diag - i

                j = diag - i
                
                if not (0 <= i <= m - 1 and 0 <= j <= n - 1):
                    continue
                    
                zigzag.append(mat[i][j])

        return zigzag