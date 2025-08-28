class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        prev_score = defaultdict(int, {0: 1})
        pref_sum = defaultdict(int, {0: 1})

        for i in range(1, n + 1):
            left = max(0, i - maxPts)
            right = min(i - 1, k - 1)

            prev_score[i] = max(0, (pref_sum[right] - pref_sum[left - 1])) * 1/maxPts
            pref_sum[i] = pref_sum[i-1] + prev_score[i]
        
        return sum([prev_score[i] for i in range(k, n+1)])