class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dif_prof = zip(difficulty, profit)
        dif_prof = sorted(dif_prof, key=lambda x: (x[0], x[1]))
        dif_prof = [(0, 0)] + dif_prof + [(inf, 0)]
        
        pref_max = defaultdict(int, {0:0})
        for i in range(1, len(dif_prof)):
            pref_max[i] = max(pref_max[i-1], dif_prof[i][1])
        
        ans = 0
        for w in worker:
            l, r = 0, len(dif_prof)
            ind = -1
            
            while l < r:
                m = (l + r) // 2
                if dif_prof[m][0] > w:   
                    ind = m
                    r = m
                else:
                    l = m + 1

            ans += pref_max[ind-1]
        
        return ans
                
                