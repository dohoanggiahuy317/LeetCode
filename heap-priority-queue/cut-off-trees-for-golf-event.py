DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])

        def bfs(start_cell, end_val):
            nonlocal forest, ans, m, n

            queue = deque([start_cell])
            reachable = set(queue)
            step = 0

            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()

                    if forest[x][y] == end_val:
                        ans += step
                        return (x, y)

                    for i, j in DIRECTIONS:
                        nx, ny = x + i, y + j

                        if not (0 <= nx < m and 0 <= ny < n):
                            continue
                        if forest[nx][ny] == 0:
                            continue
                        if (nx, ny) in reachable:
                            continue
                        
                        queue.append((nx, ny))
                        reachable.add((nx, ny))

                step += 1

            return -1

        visit_order = []
        for row in forest:
            for cell in row:
                if cell != 0 and cell != 1:
                    visit_order.append(cell)
        visit_order.sort()

        ans = 0
        start_cell = (0, 0)
        dest_idx = 0
        while dest_idx < len(visit_order):
            start_cell = bfs(start_cell, visit_order[dest_idx])
            if start_cell == -1:
                return -1
            dest_idx += 1
        
        return ans