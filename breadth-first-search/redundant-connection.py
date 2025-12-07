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
            return False
        
        if xr > yr:
            xr, yr = yr, xr

        self.parents[yr] = xr
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        dsu = DSU(len(edges))

        for x, y in edges:
            if not dsu.union(x - 1, y - 1):
                return [x, y]