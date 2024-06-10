class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [1] * len(nums)
        nums.sort()
        ans = [[i] for i in nums]


        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    if dp[j] + 1 >= dp[i]:
                        ans[i] = ans[j] + [nums[i]]
                    dp[i] = max(dp[i], dp[j] + 1)

        ans.sort(key = len)

        return ans[-1]