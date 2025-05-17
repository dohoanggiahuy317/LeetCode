class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def binarySearch(arr, val, l, r):
            if l >= r-1:
                return l

            m = (l + r) // 2
            if arr[m] < val:
                return binarySearch(arr, val, m, r)
            else:
                return binarySearch(arr, val, l, m)


        ans = -float("INF")

        for house in houses:
            dist = float("INF")
            ind = binarySearch(heaters, house, 0, len(heaters) - 1)
                
            dist = min([abs(house - heaters[max(0, ind-1)]), abs(house - heaters[ind]), abs(house - heaters[min(ind+1, len(heaters) - 1)]) ])

            ans = max(ans, dist)

        return ans