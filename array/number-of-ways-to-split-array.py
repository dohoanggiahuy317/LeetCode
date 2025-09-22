class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        suffix_sum = list(accumulate(nums[::-1]))[::-1]
        ans = 0

        for i in range(len(nums) - 1):
            ans += 1 if prefix_sum[i] >= suffix_sum[i + 1] else 0

        return ans