class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = [1] * len(s)

        for i in range(len(s)):
            curr_max = 1
            for j in range(i - 1, -1, -1):
                curr_max = max(curr_max, dp[j] + 1)
                if s[i] == s[j]:
                    dp[i] = max(dp[i], curr_max)

        return max(dp)