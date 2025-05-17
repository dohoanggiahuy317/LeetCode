class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        arr = -float("INF")

        for house in houses:
            dist = float("INF")
            for heater in heaters:
                dist = min(dist, abs(house - heater))

            arr = max(arr, dist)

        return arr