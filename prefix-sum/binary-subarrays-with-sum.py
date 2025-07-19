class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dp = defaultdict(int, {0: 1})
        curr_sum = 0
        ans = 0

        for num in nums:
            curr_sum += num
            ans += dp[curr_sum - goal]
            dp[curr_sum] += 1

        return ans

