MOD = (10 ** 9) + 7

class SegmentTree:
    def __init__(self, li):
        self.N = len(li)
        self.tree = [0] * (self.N * 2)
        self.tree[self.N:] = li
        
        for i in range(self.N - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1 )| 1]

    def query(self, l, r):
        l += self.N
        r += self.N
        ans = 0

        while l < r:
            if l & 1:
                ans += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                ans += self.tree[r]

            r >>= 1
            l >>= 1

        return ans

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        largest_power = int(math.log(n, 2))
        li = []
        while largest_power >= 0:
            if 2 ** largest_power <= n:
                li.append(largest_power)
                n -= 2 ** largest_power
            largest_power -= 1
        
        li.sort()
        ans = []
        print(li)
        tree = SegmentTree(li)
        for l, r in queries:
            ans.append(  ( 2 ** (tree.query(l, r + 1))) % MOD )

        return ans