class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc, tc = Counter(s), Counter(t)

        ans = 0
        for char in sc.keys():
            ans += (sc[char] - tc[char]) if sc[char] > tc[char] else 0

        return ans