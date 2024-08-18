class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        dp = {len(temperatures) - 1: 0}

        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] < temperatures[i+1]:
                dp[i] = 1
            else:
                if dp[i+1] == 0:
                    dp[i] = 0
                else:
                    highest = i + 1
                    while highest < len(temperatures):
                        highest += dp[highest]
                        if temperatures[i] < temperatures[highest]:
                            dp[i] = highest - i
                            break
                        elif temperatures[i] >= temperatures[highest] and dp[highest] == 0:
                            dp[i] = 0
                            break
                    if i not in dp:
                        dp[i] = 0
            
         
        ans = []
        for x in range(len(temperatures)):
            ans.append(dp[x])

        return ans

