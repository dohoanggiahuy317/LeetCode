class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        pref0 = defaultdict(int)
        suff1 = defaultdict(int)
        
        for i, ch in enumerate(s):
            pref0[i] = int(ch == '0') + pref0[i - 1]
        for i in range(n - 1, -1, -1):
            suff1[i] = int(s[i] == '1') + suff1[i + 1]
        best = 0
        for i in range(n - 1):
            best = max(best, pref0[i] + suff1[i + 1])
        return best