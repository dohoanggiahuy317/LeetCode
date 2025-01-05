import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        dp = np.array([0] * len(s))

        for st, en, di in shifts:
                dp[st:en+1] += (di*2 - 1)

        ans = ""
        for i in range(len(s)):
            ans += chr((ord(s[i]) - ord("a") + dp[i] + 26) % 26 + ord("a"))

        return ans