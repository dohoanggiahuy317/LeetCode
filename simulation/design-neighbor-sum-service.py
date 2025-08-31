class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.m, self.n = len(grid), len(grid[0])
        self.val2coor = {}
        self.coor2val = {}

        for i in range(self.m):
            for j in range(self.n):
                val = grid[i][j]
                self.val2coor[val] = (i, j)
                self.val2coor[(i, j)] = val
        

    def adjacentSum(self, value: int) -> int:
        i, j = self.val2coor[value]

        s = 0
        if i > 0:
            s += self.val2coor[(i - 1, j)]
        if i < self.m - 1:
            s += self.val2coor[(i + 1, j)]
        if j > 0:
            s += self.val2coor[(i, j - 1)]
        if j < self.n - 1:
            s += self.val2coor[(i, j + 1)]

        return s
        

    def diagonalSum(self, value: int) -> int:
        i, j = self.val2coor[value]

        s = 0
        if i > 0 and j > 0:
            s += self.val2coor[(i - 1, j - 1)]
        if i < self.m - 1 and j > 0:
            s += self.val2coor[(i + 1, j - 1)]
        if j < self.n - 1 and i < self.m - 1:
            s += self.val2coor[(i + 1, j + 1)]
        if j < self.n - 1 and i > 0:
            s += self.val2coor[(i - 1, j + 1)]

        return s


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)