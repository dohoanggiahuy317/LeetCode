class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        factor = 1
        ans = 0

        for num in nums:
            ans += num * factor
            factor *= -1

        return ans