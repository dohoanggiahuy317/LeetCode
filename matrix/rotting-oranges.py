class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        if len(rotten) == 0:
            for x in grid:
                if 1 in x:
                    return -1
            return 0

        ans = 0

        def bfs(curr_rotten):
            nonlocal ans

            ans += 1
            if curr_rotten == []:
                return 

            next_rotten = []
            for orange in curr_rotten:
                o_i, o_j = orange

                if o_i > 0 and grid[o_i - 1][o_j] == 1:
                    grid[o_i - 1][o_j] = 2
                    next_rotten.append((o_i - 1, o_j))

                if o_j > 0 and grid[o_i][o_j - 1] == 1:
                    grid[o_i][o_j - 1] = 2
                    next_rotten.append((o_i, o_j - 1))

                if o_i<m-1 and grid[o_i + 1][o_j] == 1:
                    grid[o_i + 1][o_j] = 2
                    next_rotten.append((o_i + 1, o_j))

                if o_j<n-1 and grid[o_i][o_j + 1] == 1:
                    grid[o_i][o_j + 1] = 2
                    next_rotten.append((o_i, o_j + 1))

            bfs(next_rotten)

        bfs(rotten)
        ans -= 2
        for x in grid:
            if 1 in x:
                ans = -1
                break

        return ans
    


                
