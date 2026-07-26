class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0

        for i in range(1, len(nums)):
            diff = max(0, nums[i - 1] - nums[i] + 1)
            count += diff
            nums[i] += diff

        return count