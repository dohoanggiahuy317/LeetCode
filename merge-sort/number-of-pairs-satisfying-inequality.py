class SegmentTree:
    def __init__(self, n):
        self.N = n
        self.tree = [0] * (self.N * 2)

    def update(self, i, val):
        i += self.N
        self.tree[i] = val
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

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
            
            l >>= 1
            r >>= 1
        
        return ans

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        
        nums = [x1 - x2 for x1, x2 in zip(nums1, nums2)]
        sorted_nums = sorted([(dist, i) for i, dist in enumerate(nums)])

        pos = {}
        for k_i, (snum, i) in enumerate(sorted_nums):
            k_j = bisect_left(sorted_nums, (snum - diff, -inf))
            pos[(snum, i)] = (k_i, k_j)

        ans = 0
        tree = SegmentTree(n)
        for i in range(n - 1, -1, -1):

            snum = nums[i]
            k_i, k_j = pos[(snum, i)]
            
            ans += tree.query(k_j, n)
            tree.update(k_i, 1)
            
        return ans