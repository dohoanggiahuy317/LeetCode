class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.total_cost = [(1 << 32) - 1 for _ in range(n)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y, w):
        xr, yr = self.find(x), self.find(y)
        # if xr == yr:
        #     return

        if xr > yr:
            xr, yr = yr, xr
        
        self.parents[yr] = xr
        self.total_cost[xr] = self.total_cost[xr] & self.total_cost[yr] & w
        self.total_cost[yr] = self.total_cost[xr]

        return

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = DSU(n)

        for u, v, w in edges:
            graph.union(u, v, w)
        
        ans = []
        for x, y in query:
            xr, yr = graph.find(x), graph.find(y)
            if xr == yr:
                ans.append(graph.total_cost[xr])
            else:
                ans.append(-1)

        return ans