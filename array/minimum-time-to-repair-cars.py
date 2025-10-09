class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def fixable(m):
            unfix_car = cars

            for r in ranks:
                unfix_car -= int(math.sqrt(m // r))

            return not (unfix_car > 0)

        l, r = 0, max(ranks) * (cars ** 2)
        ans = 0
        while l <= r:
            m = (l + r) // 2 
            if fixable(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans