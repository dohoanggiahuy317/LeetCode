class DSU:
    def __init__(self, N):
        self.parents = list(range(N))
        self.size = [0] * N
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        
        if xr > yr:
            xr, yr = yr, xr

        self.size[xr] += self.size[yr]
        self.size[yr] = self.size[xr]
        self.parents[yr] = xr
        # print("SUB")
        # print(self.size)
        # print()
        return

class SummaryRanges:

    def __init__(self):
        self.dsu = DSU(10 ** 4)

    def addNum(self, value: int) -> None:
        # check value - 1 and value + 1 next to it
        # merge these if both already in a set
        if self.dsu.size[value] != 0:
            return
        
        self.dsu.size[value] = 1
        if self.dsu.size[value + 1] != 0:
            self.dsu.union(value, value + 1)

        if self.dsu.size[value - 1] != 0:
            self.dsu.union(value - 1, value)

    def getIntervals(self) -> List[List[int]]:
        i = 0
        ans = []
        while i < len(self.dsu.size):
            if self.dsu.size[i] != 0:
                ans.append([i, i + self.dsu.size[i] - 1])
                i += self.dsu.size[i]
            else:
                i += 1
        # print(self.dsu.size)
        return ans
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()