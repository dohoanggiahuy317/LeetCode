class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26


        for char in s:
            idx = ord(char) - ord("a")
            curr = dp[idx]
            for i in range(max(0, idx - k), min(26, idx + k + 1)):
                curr = max(curr, dp[i] + 1)

            dp[idx] = curr

        return max(dp)

