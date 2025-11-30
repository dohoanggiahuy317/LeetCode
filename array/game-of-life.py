class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        DEAD = 0
        ALIVE = 1
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dead, alive = 0, 0
                for di, dj in DIRS:
                    ni, nj = i + di, j + dj

                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    
                    neigh_status = board[ni][nj] & 1

                    dead += (neigh_status == DEAD)
                    alive += (neigh_status == ALIVE)
                
                curr_status = board[i][j] & 1
                if curr_status == DEAD:
                    new_status = ALIVE if alive == 3 else DEAD
                else:
                    new_status = ALIVE if (alive == 2 or alive == 3) else DEAD
                
                board[i][j] = (new_status << 1) + curr_status

        for x in board:
            print([bin(cell) for cell in x])
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] >> 1
