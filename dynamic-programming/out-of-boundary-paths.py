class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        def findPathsRecursive(m, n, N, i, j):
            nonlocal memo
            if i == m or j == n or i < 0 or j < 0:
                return 1
            if N == 0:
                return 0
            if memo[i][j][N] >= 0:
                return memo[i][j][N]

            memo[i][j][N] = (
                (findPathsRecursive(m, n, N - 1, i - 1, j) + findPathsRecursive(m, n, N - 1, i + 1, j)) % M +
                (findPathsRecursive(m, n, N - 1, i, j - 1) + findPathsRecursive(m, n, N - 1, i, j + 1)) % M
            ) % M

            return memo[i][j][N]

        M = 1000000007
        memo = [[[-1 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]
        return findPathsRecursive(m, n, maxMove, startRow, startColumn)
