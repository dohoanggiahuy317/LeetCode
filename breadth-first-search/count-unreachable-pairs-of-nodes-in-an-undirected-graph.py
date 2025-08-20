class DSU:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.size = [1] * N
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)

        if xr == yr:
            return 
        
        if self.size[xr] < self.size[yr]:
            xr, yr = yr, xr

        self.parents[yr] = xr
        self.size[xr] += self.size[yr]
        self.size[yr] = self.size[xr]

        return
        

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = DSU(n)

        for u, v in edges:
            graph.union(u, v)

        roots = {graph.find(x) for x in range(n)}
        sizes = [graph.size[x] for x in roots]

        return (sum(sizes) ** 2 - sum([x ** 2 for x in sizes])) // 2