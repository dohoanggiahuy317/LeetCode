DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Constant
        m, n = len(grid), len(grid[0])
        FRESH_ORANGE = 1
        ROTTEN_ORANGE = 2
        EMPTY_ORANGE = 0

        # Set up BFS
        queue = deque()
        good_orange_left = 0
        for i, row in enumerate(grid):
            for j, orange in enumerate(row):
                if orange == FRESH_ORANGE:
                    good_orange_left += 1
                if orange == ROTTEN_ORANGE:
                    queue.append((i, j))
        reachable = set(queue)
        time = 0

        # Start BFS
        while queue or not good_orange_left:
            # Return if there is no good orange left
            if good_orange_left == 0:
                return time

            for _ in range(len(queue)):
                i, j = queue.popleft()

                for x, y in DIRECTIONS:
                    ni, nj = i + x, j + y

                    if not ( 0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] == EMPTY_ORANGE:
                        continue
                    if grid[ni][nj] == ROTTEN_ORANGE:
                        continue

                    # turn the orange to be rotten, once it get rotten
                    # by update the grid[i][j] to 2 (if not this orage will be 
                    # consider again if another rotten orange touch this)
                    grid[ni][nj] = ROTTEN_ORANGE
                    good_orange_left -= 1

                    queue.append((ni, nj))
                    reachable.add((ni, nj))
            
            time += 1 # time done after each infection round

        return -1
