class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0
        seen_x = {}
        seen_y = {}

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 1:
                    continue

                if i in seen_x or j in seen_y:
                    if i in seen_x and not seen_x[i]:
                        seen_x[i] = True
                        count -= 1
                    if j in seen_y and not seen_y[j]:
                        seen_y[j] = True
                        count -= 1
                else:
                    seen_x[i] = False
                    seen_y[j] = False
                    count += 1
                
                # print(seen_x)
                # print(seen_y)
                # print()
            
        return count