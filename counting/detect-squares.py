from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        self.grid = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.grid[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        ans = 0

        for (x2, y2), c in self.grid.items():
            if x2 != x1 or y2 == y1:
                continue

            d = abs(y2 - y1)

            ans += c * self.grid.get((x1 + d, y1), 0) * self.grid.get((x1 + d, y2), 0)
            ans += c * self.grid.get((x1 - d, y1), 0) * self.grid.get((x1 - d, y2), 0)

        return ans