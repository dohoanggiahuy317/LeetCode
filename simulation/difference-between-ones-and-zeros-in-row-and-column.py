class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = list(map(sum, grid))

        cols = list(
                map(sum, list(
                    list(
                        map(lambda x: x[i], grid)) for i in range(len(grid[0])
                        )
                    ))
                )
    
        for i in range(len(rows)):
            for j in range(len(cols)):
                grid[i][j] = 2 * rows[i] + 2 * cols[j] - len(grid) - len(grid[0])

        return grid
