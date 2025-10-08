class SegmentTree:
    def __init__(self, n):
        self.N = n
        self.tree = [0] * (2 * n)
    
    def update(self, i, x):
        i += self.N
        self.tree[i] = x
        while i > 0:
            self.tree[i >> 1] = max(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l, r):
        l += self.N
        r += self.N
        ans = 0

        while l < r:
            if (l & 1):
                ans = max(ans, self.tree[l])
                l += 1
            if (r & 1):
                r -= 1
                ans = max(ans, self.tree[r])
            
            l >>= 1
            r >>= 1

        return ans

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        sorted_nums = [..., (nums[i], i), ....]
        sorted_nums[k] = (nums[i], i) 
        -> need to find k' such that sorted_nums[k'] = (nums[j], j) 
        nums[j] < nums[i] and j < i

        create a tree represent if we see a nums[i] in the sorted_nums
        -> the segment tree gonna help to solve nums[j] < nums[i]

        loop from left to right gonna help to solve j < i
        """

        n = len(nums)
        tree = SegmentTree(n)

        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
        pos = {num: k for k, (num, i) in enumerate(sorted_nums)}

        ans = 0
        for i, num in enumerate(nums):
            k = pos[num]
            length = tree.query(0, k)

            ans = max(ans, length + 1)

            tree.update(k, length + 1)

        return ans
