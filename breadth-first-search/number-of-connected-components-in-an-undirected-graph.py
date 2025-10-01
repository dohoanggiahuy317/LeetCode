class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return 
        
        if xr < yr:
            xr, yr = yr, xr

        self.parents[yr] = xr
        return

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for a, b in edges:
            dsu.union(a, b)

        return len(set(dsu.find(i) for i in range(n)))