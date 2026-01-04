class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letter_li = list(s)
        for letter in t:
            if letter in letter_li:
                letter_li.remove(letter)
                continue
            if letter not in letter_li:
                return letter