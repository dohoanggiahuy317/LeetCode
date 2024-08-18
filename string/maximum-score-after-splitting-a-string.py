class Solution:
    def maxScore(self, s: str) -> int:
        total_one = sum(list(map(int, s)))
        total_zero = len(s) - total_one

        ans = 0

        for i in range(1, len(s)):
            ls = s[:i]
            rs = s[i:]

            rs_one = sum(list(map(int, rs)))
            ls_one = total_one - rs_one
            ls_zero = len(ls) - ls_one

            ans = max(ans, rs_one + ls_zero  )

        return ans