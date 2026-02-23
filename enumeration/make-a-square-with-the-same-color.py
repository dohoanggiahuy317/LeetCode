class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        

        m, n = len(grid), len(grid[0])
        for x in range(m - 1):
            for y in range(n - 1):
                cells = [grid[i][j], 
                         grid[i + 1][j], 
                         grid[i][j + 1], 
                         grid[i + 1][j + 1]]

                color_count = {"B": 0, "W": 0}
                for cell in cells:
                    color_count[cell] += 1
                    if color_count[cell] >= 3:
                        return True

        return False