class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        d2 = {}

        s = s.split(" ")

        for i in range(len(pattern)):
            word = pattern[i]
            term = s[i]

            if word not in d:
                d[word] = term
            else:
                if d[word] != term:
                    return False
            
            
            if term not in d1:
                d[term] = word
            else:
                if d[term] != word:
                    return False

        return True