class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        freq = Counter(s[:k])
        freq_p = Counter(p)
        ans = [0] if freq == freq_p else []

        for right in range(k, len(s)):
            freq[s[right-k]] -= 1
            freq[s[right]] += 1
            if freq == freq_p:
                ans.append(right-k+1)

        return ans