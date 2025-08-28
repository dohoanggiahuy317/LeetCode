class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)

        for diff in range(n):
            diag1 = []
            diag2 = []

            for i in range(diff, n):
                j = i - diff

                diag1.append(grid[i][j])
                diag2.append(grid[j][i])

            diag1.sort(reverse = True)
            diag2.sort()
            
            for i in range(diff, n):
                j = i - diff

                grid[i][j] = diag1[j]
                if diff != 0:
                    grid[j][i] = diag2[j]
                

        return grid


