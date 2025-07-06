class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        
        pref_max = []
        curr_max = -inf
        for d, p in jobs:
            curr_max = max(curr_max, p)
            pref_max.append(p)
        
        ans = 0
        for w in worker:
            ind = bisect_right(jobs, (w, inf))
            if ind:
                ans += pref_max[ind-1]
        
        return ans
                
                