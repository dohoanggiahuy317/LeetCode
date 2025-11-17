class SegmentTree:
    def __init__(self, n):
        self.N = n
        self.tree = [0] * (self.N * 2)
        self.tree[self.N:]

    def insert(self, i, val):
        i += self.N
        self.tree[i] = val

        while i > 0:
            self.tree[i >> 1] = max(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l, r):
        l += self.N
        r += self.N
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        sorted_nums = [...(nums[i], i),...]
        assume sorted_nums[k] = (nums[i], i)

        need to find all k' such that: 
        sorted_nums[k'] = (nums[j], j)
        nums[j'] < nums[j] and j < i

        -> the segment tree mimic the sorted_nums
        -> loop from left to right of the nums
        for each i, query the max from first index -> k index
        """

        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
        pos = {num: k for k, (num, i) in enumerate(sorted_nums)}

        ans = 0
        n = len(nums)
        segment_tree = SegmentTree(n)

        for i, num in enumerate(nums):
            k = pos[num]
            lis = segment_tree.query(0, k) + 1
            ans = max(ans, lis)
            segment_tree.insert(k, lis)

        return ans
            