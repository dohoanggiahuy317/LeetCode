class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        ans = 0

        for char, freq in count_s.items():
            ans += freq - count_t[char] if freq - count_t[char] > 0 else 0

        return ans