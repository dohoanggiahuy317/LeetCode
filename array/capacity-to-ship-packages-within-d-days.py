class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_ship(c):
            idx = 0
            for _ in range(days):
                today_c = c
                while idx < len(weights) and today_c - weights[idx] >= 0:
                    today_c -= weights[idx]
                    idx += 1

            return idx == len(weights)

        
        l, r = 0, sum(weights)
        best_c = -1

        while l <= r:
            m = (l + r) >> 1

            if can_ship(m):
                best_c = m
                r = m - 1
            else:
                l = m + 1
        
        return best_c