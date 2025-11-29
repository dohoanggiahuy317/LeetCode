class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7

        s = sum(arr)
        pref_sum = list(accumulate(arr))
        s1 = max(pref_sum)
        suff_sum = list(accumulate(arr[::-1]))
        s2 = max(suff_sum)

        if s >= 0:
            return (((max(0, (k - 2) % MOD)) * (s % MOD)) % MOD + (s1 % MOD + s2 % MOD) % MOD) % MOD

        else:
            pref_sum = list(accumulate((arr + arr) if k >= 2 else arr))
            pref_min = []

            for i, s in enumerate(pref_sum):
                pref_min.append(s if i == 0 else min(s, pref_min[-1]))
            
            ans = -inf
            for i, s in enumerate(pref_sum):
                ans = max(ans, max(s, (s - pref_min[i]) if i > 0 else s))
            
            return ans % MOD
                
                