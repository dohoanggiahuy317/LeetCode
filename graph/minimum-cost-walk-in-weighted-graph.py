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

        self.parents[yr] = xr

        self.total_cost[xr] = self.total_cost[yr] & w
        self.total_cost[yr] = self.total_cost[xr]



class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        graph = DSU(n)

        for u, v, w in edges:
            graph.union(u, v, w)

        ans = []
        for u, v in query:
            if graph.find(u) == graph.find(v):
                ans.append(graph.total_cost[graph.find(u)])
            else:
                ans.append(-1)

        return ans