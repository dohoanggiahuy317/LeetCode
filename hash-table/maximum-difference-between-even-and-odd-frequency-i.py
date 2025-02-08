
class Solution:
    def maxDifference(self, s: str) -> int:
        d = Counter(s)
        return max(_ for _ in d.values() if _ % 2 == 1) - min(_ for _ in d.values() if _ % 2 == 0)