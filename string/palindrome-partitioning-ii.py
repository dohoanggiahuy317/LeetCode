class Solution:
    def minCut(self, s: str) -> int:
        return len(Counter(s)) - 1