class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ap = defaultdict(int)
        ans = 0
        for i, char in enumerate(s):
            ap[char] = i
            if len(ap) == 3:
                ans += 1 + min(map(lambda x: x[1] , list(filter(lambda x: x[0] != char, ap.items()))))

        return ans