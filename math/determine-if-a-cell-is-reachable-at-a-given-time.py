class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        h = abs(fy - sy)
        v = abs(fx - sx)

        if max(h, v) == 0 and t == 1:
            return False


        return max(h, v) <= t
        