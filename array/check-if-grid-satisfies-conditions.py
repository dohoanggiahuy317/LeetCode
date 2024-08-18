class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        
        for i in range(m - 1):
            for j in range(len(grid[0])):
                if grid[i][j] != grid[i + 1][j]:
                    return False
        
        for i in range(m):
            for j in range(len(grid[0]) - 1):
                if grid[i][j] == grid[i][j + 1]:
                    return False
                
        return True