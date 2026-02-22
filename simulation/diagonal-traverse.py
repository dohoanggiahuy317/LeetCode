class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        UP, DOWN = 1, -1
    
        m, n = len(mat), len(mat[0])
        i, j = 0, 0
        direction = UP
        zigzag = []

        for _ in range(m * n):
            zigzag.append(mat[i][j])

            if direction == UP:
                if i == 0:
                    if j == n - 1:
                        i = 1
                    else:
                        j += 1
                    direction = DOWN
                elif j == n - 1:
                    i += 1
                    direction = DOWN
                else:
                    i -= 1
                    j += 1
            
            else:
                if j == 0:
                    if i == m - 1:
                        j = 1
                    else:
                        i += 1
                    direction = UP
                elif i == m - 1:
                    j += 1
                    direction = UP
                else:
                    i += 1
                    j -= 1

        return zigzag