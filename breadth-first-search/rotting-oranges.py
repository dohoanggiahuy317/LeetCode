class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        
        just_rotten = deque()
        num_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_fresh += 1
                if grid[i][j] == 2:
                    just_rotten.append((i, j))

        t = 0
        while just_rotten or num_fresh == 0:
            if num_fresh == 0:
                return t
            for _ in range(len(just_rotten)):
                x, y = just_rotten.popleft()
                
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy

                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if grid[nx][ny] != 1:
                        continue

                    just_rotten.append((nx, ny))
                    grid[nx][ny] = 2
                    num_fresh -= 1
            
            t += 1

        return -1