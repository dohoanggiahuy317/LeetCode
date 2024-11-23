class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        ans = [["."]*m for _ in range(n)]

        for i in range(m):
            curr = 0
            for j in range(n):
                if box[i][j] == "*":
                    ans[j][i] = "*"
                    for x in range(j-1, j-curr-1, -1):
                        ans[x][i] = "#"
                    curr = 0
                if box[i][j] == "#":
                    curr += 1
            
            for x in range(n-1, n-curr-1, -1):
                ans[x][i] = "#"
            
        ans = list(map(lambda x: x[::-1], ans))
        return ans


                
