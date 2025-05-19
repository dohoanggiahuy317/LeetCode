class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 1)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            if s[i] == "1":
                if i < len(s) - 1 and s[i+1] == "0":
                    dp[i] = dp[i+2]
                elif i < len(s) - 1:
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
            if s[i] == "2":
                if i < len(s) - 1 and s[i+1] == "0":
                    dp[i] = dp[i+2]
                elif i < len(s) - 1 and s[i+1] in "789":
                    dp[i] = dp[i+1]
                elif i < len(s) - 1:
                    dp[i] = dp[i+1] + dp[i+2]
                else:
                    dp[i] = dp[i+1]
            
        print(dp)
        return dp[0]