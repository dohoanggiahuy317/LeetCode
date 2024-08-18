class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        d = {
            'a': 0, 
            'e': 0, 
            'i': 0, 
            'o': 0, 
            'u': 0, 
            'A': 0, 
            'E': 0, 
            'I': 0, 
            'O': 0, 
            'U': 0}

        s1 = s[: len(s)//2]
        s2 = s[len(s)//2 :]

        d1 = 0
        d2 = 0

        for x in s1:
            if x in d:
                d1 += 1

        for x in s2:
            if x in d:
                d2 += 1

        return d1 == d2