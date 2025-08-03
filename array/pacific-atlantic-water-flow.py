DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])

        def bfs(sx, sy):
            nonlocal m, n, valid

            queue = deque([(sx, sy)])
            reachable = set(queue)
            pacific = atlantic = False

            while queue:
                for _ in range(len(queue)):
                    cx, cy = queue.popleft()

                    if cx == 0 or cy == 0:
                        pacific = True
                    
                    if cx == m - 1 or cy == n - 1:
                        atlantic = True

                    if ((cx, cy) in valid) or (pacific and atlantic):
                        valid.add((sx, sy))
                        return

                    for i, j in DIRECTIONS:
                        nx, ny = cx + i, cy + j

                        if not (0 <= nx <  m and 0 <= ny < n):
                            continue

                        if heights[nx][ny] > heights[cx][cy]:
                            continue
                        
                        if (nx, ny) in reachable:
                            continue

                        queue.append((nx, ny))
                        reachable.add((nx, ny))
            
            return

        valid = set()
        for i in range(m):
            for j in range(n):
                bfs(i, j)
        
        return [[x, y] for x, y in valid]

        