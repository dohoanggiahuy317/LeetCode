class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = 0

        while i < len(word) and word[i] != ch:
            i += 1

        if i == len(word):
            return word
        
        return word[0:i+1][::-1] + word[i+1:]