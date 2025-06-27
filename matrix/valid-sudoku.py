class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(row):
            t = set()
            for ele in row:
                if ele != "." and ele in t:
                    return False
                elif ele != ".":
                    t.add(ele)
            return True

        def check_square(i, j):
            nonlocal board

            square = [
                board[i][j],        board[i][j+1],      board[i][j+2],
                board[i+1][j],      board[i+1][j+1],    board[i+1][j+2],
                board[i+2][j],    board[i+2][j+1],    board[i+2][j+2],
            ]
            return check(square)

        for i in range(9):
            if not check(board[i]):
                return False
            if not check([board[j][i] for j in range(9)]):
                return False
        for i in range(0, 8, 3):
            for j in range(0, 8, 3):
                if not check_square(i, j):
                    return False

        return True
