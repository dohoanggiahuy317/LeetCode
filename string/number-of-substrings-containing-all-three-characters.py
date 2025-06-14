class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ap = defaultdict(int)
        ans = 0
        first = True
        for i, char in enumerate(s):
            l = min(map(lambda x: x[1] , list(filter(lambda x: x[0] != char, ap.items()))))
            if len(ap) == 3 and not first:
                ans += 1 + l
            ap[char] = i
            if len(ap) == 3 and first:
                ans += 1 + l
                first = False

        return ans