class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(m):
            nonlocal piles, h
            time_require = list(map(lambda x: ceil(x / m), piles))
            return sum(time_require) <= h

        l, r = 0, max(piles)
        ans = 0

        while l <= r:
            m = (l + r) // 2

            if canEat(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans