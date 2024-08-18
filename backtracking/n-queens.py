class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n
        diag1 = [False] * (2*n-1)
        diag2 = [False] * (2*n-1)
        ans = []
        table = []

        def backtrack(k):
            if k == n:
                ans.append(table[:])
                return

            for pos in range(n):
                if cols[pos] == True or diag1[k+pos] == True or diag2[n-1+pos-k]:
                    continue

                cols[pos] = True 
                diag1[k+pos] = True
                diag2[n-1+pos-k] = True
                rows = "." * pos + "Q" + "." * (n-1-pos)
                table.append(rows)

                backtrack(k+1)

                cols[pos] = False 
                diag1[k+pos] = False
                diag2[n-1+pos-k] = False
                table.pop()

        backtrack(0)
        return ans
