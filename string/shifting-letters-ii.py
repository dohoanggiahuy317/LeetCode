class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        dp = [0] * len(s)

        for st, en, di in shifts:
        
            for i in range(st, en + 1):
                dp[i] += (di*2 - 1)

        ans = ""
        for i in range(len(s)):
            ans += chr((ord(s[i]) - ord("a") + dp[i] + 26) % 26 + ord("a"))

        return ans