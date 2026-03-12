class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        row = [i for i in range(n)]
        col = [i for i in range(n, n * 2)]
        diag = [n * 2, n * 2 + 1]

        TIC_TAK_TOE_MAP = {}
        for i in range(n):
            for j in range(n):
                TIC_TAK_TOE_MAP[(i, j)] = [row[i], col[j]]

                if i == j:
                    TIC_TAK_TOE_MAP[(i, j)].append(diag[0])
                if i == n - j - 1:
                    TIC_TAK_TOE_MAP[(i, j)].append(diag[1])
            
        A_track = defaultdict(int)
        B_track = defaultdict(int)

        is_A = True

        for move in moves:
            for line in TIC_TAK_TOE_MAP[tuple(move)]:
                if is_A:
                    A_track[line] += 1
                    if A_track[line] == 3:
                        return "A"
                else:
                    B_track[line] += 1
                    if B_track[line] == 3:
                        return "B"
                
            is_A = not is_A

        return "Draw" if len(moves) == 9 else "Pending"

