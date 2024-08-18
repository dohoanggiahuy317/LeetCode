class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = {}
        d2 = {}

        for char in list(word1):
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = 1

        for char in list(word2):
            if char in d2:
                d2[char] += 1
            else:
                d2[char] = 1

        # print(d1, d2)
        # print(sorted(list(d1.keys())) == sorted(list(d2.keys())))
        # print(d1.values(), d2.values())

        return sorted(list(d1.keys())) == sorted(list(d2.keys())) and sorted(list(d1.values())) == sorted(list(d2.values()))