class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [nums[0]] * n
        suffix_sum = [nums[-1]] * n

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        for i in range(n-2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        ans = 0
        for i in range(n-1):
            if prefix_sum[i] >= suffix_sum[i + 1]:
                ans += 1
                
        return ans