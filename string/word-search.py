class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(word)
        visited = set()

        def backtrack(i, j, ind):

            if ind >= n:
                return True

            if (
                (i, j) in visited or
                i < 0 or j < 0 or
                i > len(board) - 1 or j > len(board[0]) -1 or
                word[ind] != board[i][j]
                ):
                return False

            visited.add((i, j))

            go = (
                backtrack(i-1, j, ind + 1) or
                backtrack(i+1, j, ind + 1) or
                backtrack(i, j-1, ind + 1) or
                backtrack(i, j+1, ind + 1)
            )
            visited.remove((i, j))
            return go

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0) == True:
                    return True

        return False
