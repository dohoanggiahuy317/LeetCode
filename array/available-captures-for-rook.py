class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        row_rock, col_rock = -1, -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    row_rock, col_rock = i, j
                    break

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0

        for dr, dc in DIRS:
            row = dr + row_rock
            col = dc + col_rock
            while 0 <= row <= 7 and 0 <= col <= 7:
                if board[row][col] == 'p':
                    count += 1
                    break
                elif board[row][col] != '.':
                    break
                row += dr
                col += dc
        return count