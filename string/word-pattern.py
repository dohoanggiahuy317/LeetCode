class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}

        s = s.split(" ")

        for i in range(len(pattern)):
            word = pattern[i]
            term = s[i]

            if word not in d:
                d[word] = term
            else:
                if d[word] != term:
                    return False

        return True