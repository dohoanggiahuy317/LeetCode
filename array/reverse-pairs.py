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
    def reversePairs(self, nums: List[int]) -> int:
        
        '''
        Intuition:
        Consider the sorted_list = [(nums[i], i), ..., (nums[j], j), ...]
        For each i, we need to find number of j such that:
                    i < j and nums[i] > nums[j]

        For (nums[i], i), denote sorted_list[k_i] = (nums[i], i)
        We got the index of sorted_list as list of k_i from 0 to n
        We need to find number of k_j such that
        nums[i] > nums[j] -> based on the sorted list, we can find the largest value of k_j


        Approach:
        - Created a sorted list sorted_list = [(nums[i], i), ..., (nums[j], j), ...]
        - for each index i in this sorted_list, calculate the index such that the nums
        in  sorted_list[0][0] -> sorted_list[that index][0] smaller than 1/2 of nums[i]
        - Loop in reverse order of nums, at index j, turn on the bit of the segment tree in terms
        of k_j to say we seen it
        - Later in the loop at index i, the previous bit k_j turned on can fall in the range of query if 
        this nums[i] > 2 nums[j]
        - query 0 -> k_j and update k_i
        '''


        n = len(nums)
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
        nums2k = {}
        for k_i, (num, i) in enumerate(sorted_nums):
            k_j = bisect_right(sorted_nums, ((num - 1) // 2, inf))
            nums2k[(num, i)] = (k_i, k_j)

        ans = 0
        tree = SegmentTree(n)
        for i in range(n - 1, -1, -1):
            num = nums[i]
            k_i, k_j = nums2k[(num, i)]
            ans += tree.query(0, k_j)
            tree.update(k_i, 1)
            
        return ans