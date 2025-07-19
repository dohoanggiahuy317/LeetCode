class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = defaultdict(int)
        rem_to_dp = defaultdict(int)

        for i, num in enumerate(nums):
            rem_holder = [0] * k
            for rem in range(k):
                other_num = (rem - num) % k
                past_best = rem_to_dp[(other_num, rem)] + 1
                
                dp[i] = max(dp[i], past_best)
                
                rem_holder[rem] = max(rem_holder[rem], past_best)
                rem_to_dp[(num % k, rem)] = rem_holder[rem]
            print(dp)
        return dp[len(nums) - 1]