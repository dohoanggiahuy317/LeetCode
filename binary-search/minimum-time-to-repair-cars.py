class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def check(k):
            nonlocal ranks, cars
            temp = cars
            for rank in ranks:
                temp -= int(math.sqrt(k/rank))

            return temp <= 0

        l, r = 1, min(ranks) * (cars ** 2)
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if check(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans