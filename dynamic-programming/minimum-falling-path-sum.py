class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ans = 9999999

        for i in range(1, len(matrix)):
            for j in range(len(matrix)):

                matrix[i][j] += min(
                    matrix[i-1][max(0, j - 1)], 
                    min(
                        matrix[i-1][j], 
                        matrix[i-1][min(j+1, len(matrix) - 1)])
                        )

        # print(matrix)
        
        return min(matrix[-1])

        # def backtrack(i, j, curr):
        #     nonlocal ans
        #     if i == len(matrix):
        #         ans = min(ans, curr)
        #         return

        #     backtrack(i + 1, j, curr + matrix[i][j])
        #     if j > 0:
        #         backtrack(i + 1, j - 1, curr + matrix[i][j])
        #     if j < len(matrix[0]) - 1:
        #         backtrack(i + 1, j + 1, curr + matrix[i][j])

        # for start in range(len(matrix)):
        #     backtrack(0, start, 0)

        # return ans