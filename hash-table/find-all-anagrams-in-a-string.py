class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        k = len(p)
        freq_p = Counter(p)
        freq = Counter(s[:k])
        ans = [0] if freq == freq_p else []

        for r in range(k, len(s)):

            freq[s[r]] += 1
            freq[s[r - k]] -= 1

            if freq == freq_p:
                ans.append(r - k + 1)
            
        return ans