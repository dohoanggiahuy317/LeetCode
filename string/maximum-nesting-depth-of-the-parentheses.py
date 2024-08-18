class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        count = 0

        for x in s:
            if x == ")":
                count -= 1
            elif x == "(":
                count += 1
                if count > ans:
                    ans = count

        return ans