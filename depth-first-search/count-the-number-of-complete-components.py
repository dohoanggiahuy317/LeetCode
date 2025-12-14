class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.edges = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)

        if xr == yr:
            self.edges[xr] += 1
            return

        if xr > yr:
            xr, yr = yr, xr

        self.parents[yr] = xr
        self.edges[xr] += self.edges[yr] + 1
        self.edges[yr] = self.edges[xr]

        self.size[xr] += self.size[yr]
        self.size[yr] = self.size[xr]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        dsu = DSU(n)
        for x, y in edges:
            dsu.union(x, y)

        parents = set([dsu.find(x) for x in range(n)])

        count = 0
        for parent in parents:
            si, ed = dsu.size[parent], dsu.edges[parent]
            # print(parent, si, ed, si * (si - 1) // 2)
            if (si * (si - 1) // 2) == ed:
                count += 1
        return count