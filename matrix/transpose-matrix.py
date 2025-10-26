class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m, n = len(matrix), len(matrix[0])

        ans = [[0] * m for _ in range(n)]
        # print(ans)

        for i in range(m):
            for j in range(n):
                # print(i, j)
                ans[j][i] = matrix[i][j]

        return ans