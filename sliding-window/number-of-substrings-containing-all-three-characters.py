class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        s += " "
        ap = defaultdict(int)
        ans = 0
        for i, char in enumerate(s):
            if len(ap) == 3:
                # print(i, char, ap)
                ans += min(map(lambda x: x[1] , filter(lambda x: x[0] != char, ap.items())))
                # print(ans)
            ap[char] = i
        return ans + 1