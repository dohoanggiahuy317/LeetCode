class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for x, y in coordinates:
            if y == y1:
                if x != x1:
                    return False
                continue

            if (x2 - x1)/(y2 - y1) != (x - x1)/(y - y1):
                return False

        return True