class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        freq = defaultdict(int)
        ans = 0

        for r, char in enumerate(s):
            while char in freq and freq[char] > 0:
                freq[s[l]] -= 1

                if freq[s[l]] == 0:
                    del freq[s[l]]
                
                l += 1
            
            freq[char] += 1
            ans = max(ans, r - l + 1)

        return ans


                