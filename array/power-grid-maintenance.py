class DSU:
    def __init__(self, n):
        self.N = n
        self.parent = [i for i in range(n)]
        self.recover = [[i] for i in range(n)]
        self.offline = set()

    def find(self, x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return

        if xr > yr:
            xr, yr = yr, xr

        self.parent[yr] = xr
        for avail in self.recover[yr]:
            heapq.heappush(self.recover[xr], avail)

    def shut_down(self, x):
        self.offline.add(x)

    def turn_up(self, x):
        xr = self.find(x)
        heapq.heappush(self.recover[xr], x)
        self.offline.remove(x)

    def get_nearest_recover(self, x):
        if x not in self.offline:
            return x

        xr = self.find(x)

        while self.recover[xr]:
            if self.recover[xr][0] in self.offline:
                heapq.heappop(self.recover[xr])
                continue
            
            neighbor_idx = self.recover[xr][0]
            # self.turn_up(x)
            return neighbor_idx
        
        return -1

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)

        for u, v in connections:
            dsu.union(u - 1, v - 1)

        offline = set()
        ans = []
        for query_type, idx in queries:
            idx_shift = idx - 1

            if query_type == 2:
                dsu.shut_down(idx_shift)

            else:
                recover_idx_shift = dsu.get_nearest_recover(idx_shift)
                recover_idx = recover_idx_shift + (1 if recover_idx_shift != -1 else 0)
                ans.append(recover_idx)

        return ans
                 