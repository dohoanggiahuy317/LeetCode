class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split(" ")

        for i in range(len(s)):
            if s[i].startswith(searchWord):
                return i + 1

        return -1