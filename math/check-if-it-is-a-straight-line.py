class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        a = (x2 - x1)/(y2 - y1) if y2 != y1 else 0
        b = y1 - a * x1

        return all(a * x + b == y for x, y in coordinates)