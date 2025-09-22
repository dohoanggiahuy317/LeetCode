class SegmentTree:
    def __init__(self, nums):
        self.N = len(nums)
        self.tree = [0] * (2 * self.N)
        self.tree[self.N:] = nums

        for i in range(self.N-1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[(i << 1) | 1])

    def update(self, i, x):
        i += self.N
        self.tree[i] = x
        while i > 1:
            self.tree[i >> 1] = max(self.tree[i], self.tree[i ^ 1])
            i >> 1

    def query(self, l, r):
        ans = -inf
        l += self.N
        r += self.N

        while l < r:
            if (r & 1):
                r -= 1
                ans = max(ans, self.tree[r])
            if (l & 1):
                ans = max(ans, self.tree[l])
                l += 1

            l >>= 1
            r >>= 1

        return ans

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        tree = SegmentTree(nums)

        for i in range(len(nums) - k + 1):
            val = tree.query(i, i + k)
            ans.append(val)

        return ans