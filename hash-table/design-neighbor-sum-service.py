class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.m, self.n = len(grid), len(grid[0])
        self.ADJ = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.DIA = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        self.grid = [row[:] for row in grid]
        self.value2coor = defaultdict()

        for i in range(self.m):
            for j in range(self.n):
                val = self.grid[i][j]
                self.value2coor[val] = (i, j)

    def adjacentSum(self, value: int) -> int:
        x, y = self.value2coor[value]
        ans = 0

        for dx, dy in self.ADJ:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < self.m and 0 <= ny < self.n):
                continue
            ans += self.grid[nx][ny]
        
        return ans

    def diagonalSum(self, value: int) -> int:
        x, y = self.value2coor[value]
        ans = 0

        for dx, dy in self.DIA:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < self.m and 0 <= ny < self.n):
                continue

            ans += self.grid[nx][ny]
        
        return ans


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)