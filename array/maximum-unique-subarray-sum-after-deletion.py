class Solution:
    def maxSum(self, nums: List[int]) -> int:
        return sum(filter(lambda x: x > 0, list(set(nums))))