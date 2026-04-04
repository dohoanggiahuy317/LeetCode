class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = defaultdict(lambda: -1)
        ans = 0

        for i, char in enumerate(s):
            freq[char] = i    
            if len(freq) == 3:            
                ans += 1 + min(freq.values())

        return ans
            