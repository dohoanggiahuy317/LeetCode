class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        c = 0

        for char in s:
            if char == "(":
                c += 1
            elif char == ")":
                c -= 1
            ans = max(ans, c)

        return ans