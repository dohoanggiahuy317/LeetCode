class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dp = {0: -1}
        count = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count not in dp:
                dp[count] = i
            else:
                ans = max(ans, i - dp[count]) 

        return ans


        