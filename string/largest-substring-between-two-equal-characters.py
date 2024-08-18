class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i, i]
            else:
                d[ s[i] ][1] = i

        
        return max( list( map(lambda x: x[1] - x[0] - 1, list(d.values())) ) )