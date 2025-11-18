class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)

        def hardest_job(w):
            nonlocal n

            l, r = 0, n - 1
            idx = 0

            while l <= r:
                m = (l + r) // 2
                if diff_prof[m][0] <= w:
                    idx = m
                    l = m + 1
                else:
                    r = m - 1

            return idx
            
        
        diff_prof = list(zip(difficulty, profit))
        diff_prof.sort()
        
        prof_prefix_max = list(accumulate([prof for _, prof in diff_prof], max))

        ans = 0
        for w in worker:
            if w < diff_prof[0][0]:
                continue

            idx = hardest_job(w)
            ans += prof_prefix_max[idx]

        return ans
