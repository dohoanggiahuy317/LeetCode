class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            row_set = set()

            for cell in row:
                if cell in row_set:
                    return False
                if cell != ".":
                    row_set.add(cell)

        for col_idx in range(9):
            col_set = set()

            for row in board:
                if row[col_idx] in col_set:
                    return False
                if row[col_idx] != ".":
                    col_set.add(row[col_idx])

        DIRS = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
            ]

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                square_set = set()

                for di, dj in DIRS:
                    ni, nj = i + di, j + dj

                    if board[ni][nj] in square_set:
                        return False
                    
                    if board[ni][nj] != ".":
                        square_set.add(board[ni][nj])

        return True
                

        