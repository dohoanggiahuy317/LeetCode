class Solution:
    def maxScore(self, s: str) -> int:
        pref_0 = []
        suff_1 = []

        for i, char in enumerate(s):
            pref_0.append(int(char == "0") + (pref_0[i - 1] if i > 0 else 0))

        for i, char in enumerate(s[::-1]):
            suff_1.append(int(char == "1") + (suff_1[i - 1] if i > 0 else 0))

        suff_1 = suff_1[::-1]

        best_score = 0

        for i in range(len(s) - 1):
            best_score = max(best_score, pref_0[i] + suff_1[i + 1])

        return best_score