class Solution:
    def longestBalanced(self, s: str) -> int:

        n = len(s)
        dp = [[0] * n for _ in range(3)]

        for o in range(3):
            for i, char in enumerate(s):
                if o == ord(char) - ord("a"):
                    dp[o][i] = 1 + (dp[o][i - 1] if i > 0 else 0)
                else:
                    dp[o][i] = (dp[o][i - 1] if i > 0 else 0)

        
        ans = 1
        for i in range(n-1, -1, -1):
            for j in range(i):
                freq = set([dp[k][i] - (dp[k][j - 1] if j > 0 else 0) for k in range(3)])
                if 0 in freq:
                    freq.remove(0)
                if len(freq) == 1:
                    ans = max(ans, i - j + 1)
                    break

        return ans