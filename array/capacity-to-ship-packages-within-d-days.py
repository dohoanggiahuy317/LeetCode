class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(m):
            nonlocal weights, days

            curr_sum = 0
            day_need = 1
            for weight in weights:
                curr_sum += weight
                if curr_sum > m:
                    curr_sum = weight
                    day_need += 1
                
                # print(curr_sum)

            # day_need += 1 if curr_sum > m else 0

            return day_need <= days

        l, r = max(weights), sum(weights)
        ans = 0
        while l <= r:
            m = (l + r) // 2
            print(l, r, m)
            if canShip(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans