class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        curr = 0

        for i in range(0, len(nums)//2 + 1):
            curr = max(curr, nums[i] + nums[len(nums) - 1 - i] )

        return curr
        