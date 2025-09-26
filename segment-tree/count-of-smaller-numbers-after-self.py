class SegmentTree:
    def __init__(self, n):
        self.N = n
        self.tree = [0] * (self.N * 2)

    def update(self, i, val):
        i += self.N
        self.tree[i] = val
        while i > 0:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1
    
    def query(self, l, r):
        ans = 0
        l += self.N
        r += self.N
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
    def countSmaller(self, nums: List[int]) -> List[int]:

        # Intuition: 
        # For each index j, we need to count how many index j' such that
        #           j < j' and nums[j] > nums[j']
        # This means
        # if value_index[k] = [(nums[j], j)], then number of j' = number of k'
        # as nums[j] > nums[j'], so k > k'
        #
        # For each k, we will try to find number of k'
        # 
        # Approach:
        # -> if we loop backwards of nums, we will get a sequence of k_0, k_1, ...k_n
        # where k_i just the index from 0 to n
        #
        # At a point a we check k_a, all the k_i that is seen before k_a means the  
        # number in nums corresponding with k_i comes after k_a (we loop backwards of nums)
        # 
        # Also as we only care nums[i] < nums[a] -> k_a = sum of all value k_i from 0 to k_a - 1


        n = len(nums)
        nums2k = {}
        for k, num in enumerate(sorted(nums)):
            nums2k[num] = k

        ans = []
        tree = SegmentTree(n)

        for i in range(n - 1, -1, -1):
            num = nums[i]
            k = nums2k[num]
            ans = [tree.query(0, k)] + ans
            tree.update(k, 1)
        
        return ans