class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        
        DIRS = [ ((-1, -1), (-1, 0)), 
                 ((-1, 1),  (0, 1)),
                 ((1, 1),   (1, 0)),
                 ((1, -1),  (0, -1)),
                 ((0, -1),  (-1, -1))
                ]

        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n): # iterate thru each cell
                cell_color = grid[x][y]

                for rect in DIRS: # check all neighbor 2x1 rect
                    for dx, dy in rect: # check each cell
                        nx, ny = x + dx, y + dy

                        if not (0 <= nx < m and 0 <= ny < n):
                            break
                        if grid[nx][ny] != cell_color:
                            break
                    else:
                        return True

        return False