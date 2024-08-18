class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(i):
            nonlocal board

            row = board[i]
            s = set()

            for x in row:
                if x != ".":
                    if x not in s:
                        s.add(x)
                    else:
                        return False
            
            return True

        def check_col(i):
            nonlocal board

            col = list(map(lambda x: x[i], board))
            s = set()

            for x in col:
                if x != ".":
                    if x not in s:
                        s.add(x)
                    else:
                        return False
            
            return True

        def check_square(i, j):
            nonlocal board

            square = [
                board[i-1][j-1], board[i-1][j], board[i-1][j+1],
                board[i][j-1],   board[i][j],   board[i][j+1],
                board[i+1][j-1], board[i+1][j], board[i+1][j+1],
            ]

            s = set()
            for x in square:
                if x != ".":
                    if x not in s:
                        s.add(x)
                    else:
                        return False
            
            return True


        for i in range(9):
            if not check_row(i) or not check_col(i):
                return False

        if (
            not check_square(1, 1) or not check_square(1, 4) or not check_square(1, 7)
        ) or (
            not check_square(4, 1) or not check_square(4, 4) or not check_square(4, 7)
        ) or (
            not check_square(7, 1) or not check_square(7, 4) or not check_square(7, 7)
        ): 
            return False
        
        return True
