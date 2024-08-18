class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def sum_check(i, j):
            row, col, diag = 0, 0, 0

            if sum([grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1]]) == sum([grid[i][j-1],grid[i][j],grid[i][j+1]]) == sum([grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]]):
                row = sum([grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1]])
            else:
                return False

            if sum([grid[i-1][j-1],grid[i][j-1],grid[i+1][j-1]]) == sum([grid[i-1][j],grid[i][j],grid[i+1][j]]) == sum([grid[i-1][j+1],grid[i][j+1],grid[i+1][j+1]]):
                col = sum([grid[i-1][j-1],grid[i][j-1],grid[i+1][j-1]])
            else:
                return False

            if sum([grid[i-1][j-1],grid[i][j],grid[i+1][j+1]]) == sum([grid[i+1][j-1],grid[i][j],grid[i-1][j+1]]):
                diag = sum([grid[i-1][j-1],grid[i][j],grid[i+1][j+1]])
            else:
                return False

            if row == col == diag:
                return True

            return False

        invalid = set()

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] > 9 or grid[i][j] < 1:
                    invalid.add((i, j))

        ans = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                check = True
                temp = set()

                for x in [i-1, i, i+1]:
                    for y in [j-1, j, j+1]:
                        if check:
                            temp.add(grid[x][y])
                            if (x, y) in invalid:
                                check = False
                                break
                if check:
                    if len(temp) == 9 and sum_check(i, j):
                        ans += 1

        return ans