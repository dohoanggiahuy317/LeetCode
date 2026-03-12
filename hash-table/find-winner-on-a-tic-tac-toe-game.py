class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        ROW1, ROW2, ROW3 = 0, 1, 2
        COL1, COL2, COL3 = 4, 5, 6
        DIA1, DIA2 = 7, 8

        TIC_TAK_TOE_MAP = {
            (0, 0): [ROW1, COL1, DIA1],
            (0, 1): [ROW1, COL2],
            (0, 2): [ROW1, COL3, DIA2],
            (1, 0): [ROW2, COL1],
            (1, 1): [ROW2, COL2, DIA1, DIA2],
            (1, 2): [ROW2, COL3],
            (2, 0): [ROW3, COL1, DIA2],
            (2, 1): [ROW3, COL2],
            (2, 2): [ROW3, COL3, DIA1]
        }

        A_track = { # How many X of each
            ROW1: 0, ROW2: 0, ROW3: 0, COL1: 0, COL2: 0, COL3: 0, DIA1: 0, DIA2: 0
        }
        B_track = { # How many X of each
            ROW1: 0, ROW2: 0, ROW3: 0, COL1: 0, COL2: 0, COL3: 0, DIA1: 0, DIA2: 0
        }

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

        return "Draw"

