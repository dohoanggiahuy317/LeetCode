class DSU:
    def __init__(self, m, n):
        self.M, self.N = m, n
        self.parent = [[(i, j) for j in range(n)] for i in range(m)]

    def find(self, x, y):
        if self.parent[x][y] == (x, y):
            return (x, y)
        xr, yr = self.parent[x][y]
        self.parent[x][y] = self.find(xr, yr)

        return self.parent[x][y]

    def union(self, x1, y1, x2, y2):
        xr1, yr1 = self.parent[x1][y1]
        xr2, yr2 = self.parent[x2][y2]

        if (xr1, yr1) == (xr2, yr2):
            return False

        if yr1 > yr2:
            xr1, xr2 = xr2, xr1
            yr1, yr2 = yr2, yr1
        
        if xr1 > xr2:
            xr1, xr2 = xr2, xr1
            yr1, yr2 = yr2, yr1

        self.parent[xr2][yr2] = (xr1, yr1)
        return True
        
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = DSU(m, n)
        board = [[0] * n for _ in range(m)]
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        ans = []
        island_num = 0
        for x, y in positions:
            board[x][y] = 1
            island_num += 1

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                
                if board[nx][ny] != 1:
                    continue

                if dsu.union(x, y, nx, ny):
                    island_num -= 1

            ans.append(island_num)

        return ans

