class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        p = set()
        a = set()

        def bfs(i, j, sea, prevHeight):
            nonlocal m, n, heights   
            if (
                i < 0 or
                j < 0 or
                i > m - 1 or
                j > n - 1 or 
                (i, j) in sea or
                heights[i][j] < prevHeight
            ):
                return

            sea.add((i, j))

            bfs(i+1, j, sea, heights[i][j])
            bfs(i-1, j, sea, heights[i][j])
            bfs(i, j+1, sea, heights[i][j])
            bfs(i, j-1, sea, heights[i][j])

        for i in range(m):
            bfs(i, 0, p, heights[i][0])
            bfs(i, n-1, a, heights[i][n-1])

        for i in range(n):
            bfs(0, i, p, heights[0][i])
            bfs(m-1, i, a, heights[m-1][i])

        ans = []
        for i in p:
            if i in a:
                ans.append(i)

        return ans
