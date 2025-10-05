class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        dp[-1] = 1 if s[-1] != "0" else 0

        for i in range(len(s) - 2, -1, -1):
            if s[i] == "0":
                dp[i] = 0

            elif s[i] not in "12":
                if s[i + 1] == "0" and i + 2 >= len(s):
                    dp[i] = 1
                else:
                    dp[i] = dp[i + 1]

            elif s[i] == "1":
                if s[i + 1] == "0" and i + 2 >= len(s):
                    dp[i] = 1
                elif s[i + 1] == "0":
                    dp[i] = dp[i + 2] if i + 2 < len(s) else 1
                elif i + 2 < len(s) and s[i + 2] == "0":
                    dp[i] =  [i + 2]
                else:
                    dp[i] = dp[i + 1] + 1
            
            elif s[i] == "2":
                if s[i + 1] == "0" and i + 2 >= len(s):
                    dp[i] = 1
                elif s[i + 1] in "0789":
                    dp[i] = dp[i + 2] if i + 2 < len(s) else 1
                elif  (i + 2 < len(s) and s[i + 2] == "0"):
                    dp[i] = dp[i + 1]
                else:
                    dp[i] = dp[i + 1] + 1

        # print(dp)
        return dp[0]

