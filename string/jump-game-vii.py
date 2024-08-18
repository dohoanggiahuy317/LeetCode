class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[0] != '0' or s[-1] != '0':
            return False

        dp = [c == '0' for c in s]
        curr = 0

        for i in range(1, len(s)):
            # print(curr)
            if i >= minJump:
                curr = curr + dp[i - minJump]
            if i > maxJump:
                curr = curr - dp[i - maxJump - 1]
            dp[i] = dp[i] & (curr > 0)

        # print(dp)

        return dp[-1]

        