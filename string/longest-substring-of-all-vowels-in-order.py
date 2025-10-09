class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        l, r = 0, 0
        num_vowel = 1
        ans = 0
        
        for r in range(n):
            if r > l and ord(word[r]) >= ord(word[r - 1]):
                if ord(word[r]) > ord(word[r - 1]):
                    num_vowel += 1
                if num_vowel == 5:
                    ans = max(ans, r - l + 1)
            else:
                l = r
                num_vowel = 1

        return ans

        