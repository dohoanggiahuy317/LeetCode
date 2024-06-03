class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        start = 0

        for x in s:
            # print(x, s[start], start)
            if start >= len(t):
                return 0
            if x == t[start]:
                start += 1

        return len(t) - start