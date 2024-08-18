class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])

        visited = set()

        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:

                    visited.add((i, j))

                    if land[i][j] == 0:
                        continue

                    ite1 = 1
                    while i + ite1 < m and land[i + ite1][j] == 1:
                        ite1 += 1
                    ite2 = 1
                    while j + ite2 < n and land[i][j + ite2] == 1:
                        ite2 += 1
                    
                    for x_i in range(i, i + ite1):
                        for x_j in range(j, j + ite2):
                            visited.add((x_i, x_j))

                    ans.append([i, j, i + ite1 - 1, j + ite2 - 1])

        return ans
