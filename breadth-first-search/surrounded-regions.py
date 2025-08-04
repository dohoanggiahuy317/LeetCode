DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def bfs(sx, sy):
            nonlocal invalid, m, n, board

            if board[sx][sy] == "X":
                return

            queue = deque([ (sx, sy) ])
            reachable = set(queue)

            while queue:
                for _ in range(len(queue)):
                    cx, cy = queue.popleft()
                    invalid.add((cx, cy))

                    for i, j in DIRECTIONS:
                        nx, ny = cx + i, cy + j
                        
                        if not (0 <= nx < m and 0 <= ny < n):
                            continue
                        
                        if board[nx][ny] == "X":
                            continue

                        if (nx, ny) in reachable:
                            continue

                        queue.append((nx, ny))
                        reachable.add((ny, ny))

        
        m, n = len(board), len(board[0])
        invalid = set()

        for i in range(m):
            bfs(i, 0)
            bfs(i, n - 1)
            
        for j in range(n):
            bfs(0, j)
            bfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in invalid:
                    board[i][j] = "X"

        return 
