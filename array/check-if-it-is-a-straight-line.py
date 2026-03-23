class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x1 == x2:
            return all(x == x1 for x, _ in coordinates)

        a = (y2 - y1)/(x2 - x1)
        b = y1 - a * x1

        return all(a * x + b == y for x, y in coordinates)