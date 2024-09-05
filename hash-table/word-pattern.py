class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        d1 = {}

        s = s.split(" ")

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            word = pattern[i]
            term = s[i]

            if word not in d:
                d[word] = term
            else:
                if d[word] != term:
                    return False
            
            
            if term not in d1:
                d1[term] = word
            else:
                if d1[term] != word:
                    return False

        return True