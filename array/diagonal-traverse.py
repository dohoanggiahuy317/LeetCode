class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []

        for diag in range(m + n - 1):
            if diag % 2 == 1:
                for i in range(diag + 1):
                    j = diag - i

                    if not (0 <= i < m and 0 <= j < n):
                        continue
                    ans.append(mat[i][j])
            else:
                for i in range(diag, -1, -1):
                    j = diag - i

                    if not (0 <= i < m and 0 <= j < n):
                        continue
                    ans.append(mat[i][j])
                
        return ans