class Solution:
    def maxScore(self, s: str) -> int:

        n = len(s)
        pref_0 = [0] * n
        suff_1 = [0] * n
        
        for i, char in enumerate(s):
            pref_0[i] = int(char == "0") + (pref_0[i - 1] if i > 0 else 0)
            
        for i in range(n - 1, -1, -1):
            char = s[i]
            suff_1[i] = int(char == "1") + (suff_1[i + 1] if i < n - 1 else 0)
                    
        best_score = 0
        for i in range(n - 1):
            best_score = max(best_score, pref_0[i] + suff_1[i + 1])
            
        return best_score
                        