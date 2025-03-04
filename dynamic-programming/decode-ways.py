class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        s += " "

        for i in range(len(s)-2, -1, -1):
            # print(i, s[i])
            if s[i] == "2":
                if s[i+1] in "123456":
                    if i + 2 < len(s) and s[i+2] == "0":
                        dp[i] = dp[i+1]
                    else:
                        dp[i] = dp[i+1] + 1
                else:
                    dp[i] = dp[i+1]
            
            elif s[i] == "1":
                if i + 2 < len(s) and s[i+2] == "0":
                        dp[i] = dp[i+1]
                else:
                    dp[i] = dp[i+1] + 1
            
            else:
                if s[i+1] == "0":
                    return 0
                dp[i] = dp[i+1]

        # print(dp)
        return dp[0]