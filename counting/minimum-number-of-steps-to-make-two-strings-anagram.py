class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict, t_dict = Counter(s), Counter(t)
        ans = 0

        for char, freq in s_dict.items():
            if freq > t_dict[char]:
                ans += freq - t_dict[char]

        return ans