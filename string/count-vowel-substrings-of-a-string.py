class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        freq = defaultdict()
        ans = 0
        l = 0

        for r, char in enumerate(word):
            if char in "ueoai":
                freq[char] = r

                if len(freq) == 5:
                    ans += min(freq.values()) - l + 1
            else:
                l = r + 1
                freq = {}
            
        return ans