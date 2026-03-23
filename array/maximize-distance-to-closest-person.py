class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        anchor = -1
        best_dist = 0

        for i, seat in enumerate(seats):
            if seat != 1:
                continue

            if anchor == -1:
                best_dist = max(best_dist, i)
            else:
                best_dist = max(best_dist, (i - anchor) // 2)

            anchor = i

        return max(best_dist, n - anchor - 1)
            
    

