class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack(cell_idx):
            nonlocal board, rows, cols, sqrs, empty

            if cell_idx == len(empty):
                return True
            
            i, j = empty[cell_idx]
        
            for num in "123456789":
                if num in rows[i]:
                    continue
                if num in cols[j]:
                    continue
                if num in sqrs[i // 3 * 3 + j // 3]:
                    continue
                
                board[i][j] = num
                rows[i].add(num)
                cols[j].add(num)
                sqrs[i // 3 * 3 + j // 3].add(num)

                if backtrack(cell_idx + 1):
                    return True
                
                rows[i].remove(num)
                cols[j].remove(num)
                sqrs[i // 3 * 3 + j // 3].remove(num)

            return False

        
        rows, cols, sqrs = defaultdict(set), defaultdict(set), defaultdict(set)
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    
                    idx = i // 3 * 3 + j // 3
                    sqrs[idx].add(board[i][j])
                else:
                    empty.append((i, j))

        backtrack(0)
