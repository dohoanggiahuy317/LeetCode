class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def fixable(m):
            c = cars

            for r in ranks:
                c -= int(math.sqrt(m // r))

            return not (c > 0)

        mi, ma = 0, max(ranks) * (cars ** 2)
        ans = 0
        while mi <= ma:
            m = (mi + ma) // 2 
            if fixable(m):
                ans = m
                ma = m - 1
            else:
                mi = m + 1

        return ans