class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        ans = 0
        
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    grid[i][j] = 1 - grid[i][j]

        ans += 2 ** (len(grid[0]) - 1) * len(grid)

        for j in range(1, len(grid[0])):
            curr_sum = sum(list(map(lambda x: x[j], grid)))
            max_bin = max(len(grid) - curr_sum, curr_sum)
            ans += 2 ** (len(grid[0]) - j - 1) * max_bin

        return ans