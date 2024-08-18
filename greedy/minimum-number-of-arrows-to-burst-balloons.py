class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        arrows = n = len(points)
        i = 0
        while i < n -1:
            edge = points[i][1]
            while i < n - 1 and edge >= points[i+1][0]:
                arrows -= 1
                i += 1
            i += 1

        return arrows