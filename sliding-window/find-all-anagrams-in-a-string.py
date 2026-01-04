class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k, n = len(p), len(s)
        freq_p = Counter(p)
        freq_sub_s = Counter(s[:k])
        ans = [0] if freq_p == freq_sub_s else []

        for r in range(k, n):
            freq_sub_s[s[r]] += 1
            freq_sub_s[s[r - k]] -= 1

            if freq_sub_s == freq_p:
                ans.append(r - k + 1)

        return ans