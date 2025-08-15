DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # CONSTANT
        m, n = len(heights), len(heights[0])

        # BFS
        def bfs(sx, sy, from_pacific):
            nonlocal m, n, flow_to_pacific, valid_cell

            queue = deque([(sx, sy)])
            reachable = set(queue)

            while queue:
                for _ in range(len(queue)):
                    cx, cy = queue.popleft()

                    if from_pacific:
                        flow_to_pacific[cx][cy] = True
                    else:
                        if flow_to_pacific[cx][cy] == True:
                            valid_cell.add((cx, cy))

                    for i, j in DIRECTIONS:
                        nx, ny = cx + i, cy + j

                        if not (0 <= nx < m and 0 <= ny < n):
                            continue

                        if heights[nx][ny] < heights[cx][cy]:
                            continue
                        
                        if (nx, ny) in reachable:
                            continue

                        queue.append((nx, ny))
                        reachable.add((nx, ny))
            
            return


        valid_cell = set() # answer
        flow_to_pacific = [[False] * n for _ in range(m)]

        # GO FROM SHORE FROM PACIFIC
        for i in range(m):
            bfs(i, 0, from_pacific = True)
        for j in range(n):
            bfs(0, j, from_pacific = True)

        # GO FROM SHORE FROM ATLANTIC
        for i in range(m):
            bfs(i, n-1, from_pacific = False)
        for j in range(n):
            bfs(m-1, j, from_pacific = False)
        
        return [[x, y] for x, y in valid_cell]

        