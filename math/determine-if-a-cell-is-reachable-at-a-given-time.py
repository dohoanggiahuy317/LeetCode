class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        a, b = abs(fy - sy), abs(fx - sx)
        if max(a, b) == 0 and t == 1:
            return False
        return max(a, b) <= t
        