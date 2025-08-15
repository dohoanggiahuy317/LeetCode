DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def bfs(board_borders):
            nonlocal invalid, m, n, board

            queue = deque(board_borders)
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
                        reachable.add((nx, ny))

        # CONSTANT
        m, n = len(board), len(board[0])
        invalid = set()

        # BFS
        board_borders = []
        for i in range(m):
            if board[i][0] == "O":
                board_borders.append((i, 0))
            if board[i][n-1] == "O":
                board_borders.append((i, n-1))

        for j in range(n):
            if board[0][j] == "O":
                board_borders.append((0, j))
            if board[m-1][j] == "O":
                board_borders.append((m-1, j))

        bfs(board_borders)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in invalid:
                    board[i][j] = "X"

        return 
