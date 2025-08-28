class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        def backtrack(row_ith, table):
            nonlocal n, cols, diags1, diags2

            if row_ith == n:
                ans.append(table[:])
                return

            for pos in range(n):
                if cols[pos]:
                    continue
                if diags1[row_ith + pos]:
                    continue
                if diags2[n - 1 - row_ith + pos]:
                    continue

                cols[pos] = True 
                diags1[pos + row_ith] = True
                diags2[n - 1 - row_ith + pos] = True
                table.append("." * pos + "Q" + "." * (n - 1 - pos))

                backtrack(row_ith + 1, table)

                cols[pos] = False 
                diags1[pos + row_ith] = False
                diags2[n - 1 - row_ith + pos] = False
                table.pop()


        cols = [False] * n
        diags1 = [False] * (2 * n - 1) # diag of / direction
        diags2 = [False] * (2 * n - 1) # diag of \ direction
        ans = []
        backtrack(0, [])
        return ans
