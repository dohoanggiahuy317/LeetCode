class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = defaultdict(int)
        rem_to_dp = defaultdict(int)

        for i, num in enumerate(nums):
            for rem in range(k):
                other_num = (rem - num) % k
                dp[i] = max(dp[i], rem_to_dp[(other_num, rem)] + 1)
                value_track[(num % k, rem)] = dp[i]

        return dp[len(nums) - 1]