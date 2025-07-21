class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dp = defaultdict(int, {0: 1})
        cur, ans = 0, 0
        for i, num in enumerate(nums):
            cur += num
            ans += dp[cur-goal]
            dp[cur] += 1
        return ans