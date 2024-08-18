class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        for i in range(len(self.grid)):
            if value in self.grid[i]:
                j = self.grid[i].index(value)
                break
        
        ans = 0
        if i > 0:
            ans += self.grid[i-1][j]
        if i < len(self.grid) - 1:
            ans += self.grid[i+1][j]
        if j > 0:
            ans += self.grid[i][j-1]
        if j < len(self.grid[0]) - 1:
            ans += self.grid[i][j+1]

        return ans

    def diagonalSum(self, value: int) -> int:
        for i in range(len(self.grid)):
            if value in self.grid[i]:
                j = self.grid[i].index(value)
                break
        
        ans = 0
        if i > 0 and j < len(self.grid[0]) - 1:
            ans += self.grid[i-1][j+1]
        if i > 0 and j > 0:
            ans += self.grid[i-1][j-1]
        if i < len(self.grid) - 1 and j < len(self.grid[0]) - 1:
            ans += self.grid[i+1][j+1]
        if i < len(self.grid) - 1 and j > 0:
            ans += self.grid[i+1][j-1]

        return ans


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)