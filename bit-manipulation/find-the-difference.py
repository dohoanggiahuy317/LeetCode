class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for char, freq in t_counter.items():
            if freq != s_counter[char]:
                return char

        return ""