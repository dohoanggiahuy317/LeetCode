class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        
        TOP_LEFT = [(-1, -1), (-1, 0), (0, -1)]
        TOP_RIGHT = [(-1, 0), (-1, 1), (0, 1)]
        BOT_LEFT = [(0, -1), (-1, 1), (1, 0)]
        BOT_RIGHT = [(1, 0), (1, 1), (0, 1)]
        DIRS = [TOP_LEFT, TOP_RIGHT, BOT_LEFT, BOT_RIGHT]

        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n): # iterate thru each cell
                
                for orient in DIRS: # check all directions
                    for dx, dy in orient: # check each neighbor cell
                        nx, ny = x + dx, y + dy

                        if not (0 <= nx < m and 0 <= ny < n):
                            break
                        if grid[nx][ny] == "B":
                            break
                    else:
                        return True

        return False