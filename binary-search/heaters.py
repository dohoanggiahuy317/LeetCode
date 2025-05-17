class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        arr = []

        for house in houses:
            dist = []
            for heater in heaters:
                dist.append(abs(house - heater))

            arr.append(dist)

        return max(list(map(lambda x: min(x), arr)))