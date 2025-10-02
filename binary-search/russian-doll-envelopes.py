class SegmentTree:
    def __init__(self, n):
        self.N = n
        self.tree = [0] * (2 * self.N)

    def update(self, i, x):
        i += self.N
        self.tree[i] = x
        while i > 1:
            self.tree[i >> 1] = max(self.tree[i], self.tree[i ^ 1])
            i >>= 1
    def query(self, l, r):
        ans = 0
        l += self.N
        r += self.N
        while l < r:
            if (l & 1):
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
                
            l >>= 1
            r >>= 1
        return ans

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        envelopes_y = sorted([y for _, y in envelopes])
        # print(envelopes)
        # print(envelopes_y)
        n = len(envelopes)
        tree = SegmentTree(n)        

        ans = 1
        for i in range(n):
            x, y = envelopes[i]

            y_idx = bisect_left(envelopes_y, y)
        
            best = tree.query(0, y_idx) + 1
            ans = max(ans, best)

            tree.update(y_idx, best)

        return ans




