class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum( [ x-1 for x in list(Counter(word).values())] ) + 1