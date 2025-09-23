class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        prefix_max = [nums[0]] * len(nums)
        prefix_min = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            prefix_max[i] = max(prefix_max[i - 1], prefix_sum[i])
            prefix_min[i] = min(prefix_min[i - 1], prefix_sum[i])
        # print(prefix_sum)
        # print(prefix_max)
        # print(prefix_min)
        ans = -inf
        for i in range(len(nums)):
            ans = max(ans, prefix_max[i])
            ans = max(ans, prefix_max[i] - prefix_min[i - 1] if i > 0 else 0)

        return ans