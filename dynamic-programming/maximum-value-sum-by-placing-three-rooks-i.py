class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        max_sum = float('-inf')

        max_row_vals = [max(row) for row in board]
        
        def backtrack(row, rooks_placed, curr_sum, columns):
            nonlocal max_sum
            
            if rooks_placed == 3:
                max_sum = max(max_sum, curr_sum)
                return
            
            if row >= m:
                return
            
            remaining_possible_sum = curr_sum + sum(sorted(max_row_vals[row:m])[-(3-rooks_placed):])
            if remaining_possible_sum <= max_sum:
                return
            
            for col in range(n):
                if col not in columns:
                    columns.add(col)
                    backtrack(row + 1, rooks_placed + 1, curr_sum + board[row][col], columns)
                    columns.remove(col)
            
            backtrack(row + 1, rooks_placed, curr_sum, columns)

        backtrack(0, 0, 0, set())
        
        return max_sum