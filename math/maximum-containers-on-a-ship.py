class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return n * n if n * n * w <= maxWeight else maxWeight // w