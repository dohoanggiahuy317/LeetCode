class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * 10001

        for i in nums:
            dp[i] += i

        s1 = s2 = 0

        for i in dp:
            s1, s2 = s2, max(s1+i, s2)
        
        return s2