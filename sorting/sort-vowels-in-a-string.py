class Solution:
    def sortVowels(self, s: str) -> str:
        d = {
            "u": 0,
            "e": 0,
            "o": 0,
            "a": 0,
            "i": 0,
            "U": 0,
            "E": 0,
            "O": 0,
            "A": 0,
            "I": 0
        }
        pos = []
        vow = []

        for i in range(len(s)):
            if s[i] in d.keys():
                pos.append(i)
                vow.append(s[i])

        vow.sort()
        # print(pos)
        # print(vow)

        for i in range(len(pos)):
            if pos[i] < len(s) - 1:
                s = s[:pos[i]] + vow[i] + s[pos[i]+1:]
            else:
                s = s[:pos[i]] + vow[i]


        return s
        

        