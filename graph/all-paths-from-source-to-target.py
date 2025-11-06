class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        def dfs(x):
            nonlocal graph, n, ans, path
            if x == n - 1:
                path.append(x)
                ans.append(path[:])
                path.pop()
                return

            path.append(x)
            for neigh in graph[x]:
                dfs(neigh)
            path.pop()


        ans = []
        path = []
        dfs(0)
        return ans