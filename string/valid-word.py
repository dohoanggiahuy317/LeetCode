class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        if not word.isalnum():
            return False

        b = c = False

        for w in word:
            if w in "ueoaiUEOAI":
                b = True
            if w.isalpha() and w not in "ueoaiUEOAI":
                c = True

        return b and c