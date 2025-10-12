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

        if xr > yr:
            xr, yr = yr, xr

        self.parents[yr] = xr


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)
        for x, y in pairs:
            dsu.union(x, y)

        idx_group = defaultdict(list)
        idx_char = defaultdict(list)
        for i, char in enumerate(s):
            idx_char[dsu.find(i)].append(char)
            idx_group[dsu.find(i)].append(i)

        ans = [""] * n

        for i, char_li in idx_char.items():
            idx_char[i] = sorted(char_li)

        for idx_li, char_li in zip(idx_group.values(), idx_char.values()):
            for j in range(len(idx_li)):
                ans[idx_li[j]] = char_li[j]

        return "".join(ans)



