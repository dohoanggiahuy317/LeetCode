class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = [[float("inf")] * (k + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0

        for i in range(1, len(s) + 1):
            for j in range(k + 1):
                if j > 0:
                    dp[i][j] = dp[i-1][j-1]

                count = 0
                del_count = 0

                for l in range(i, 0, -1):
                    if s[l-1] == s[i-1]:
                        count += 1
                    else:
                        del_count += 1
                    if del_count > j:
                        break

                    encode = 1 + (len(str(count)) if count > 1 else 0)
                    dp[i][j] = min(dp[i][j], dp[l - 1][j - del_count] + encode)

        return dp[len(s)][k]
