# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        ans = -1

        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                ans = r
                r -= 1
            else:
                l += 1

        return ans