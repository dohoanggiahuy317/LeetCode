class Solution:
    def maxSum(self, nums: List[int]) -> int:
        t = sorted(list(set(nums)), reverse = True)
        ans = float("-inf")
        for x in accumulate(t):
            ans = max(ans, x)
        return ans