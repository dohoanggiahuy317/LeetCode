class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dif_prof = zip(difficulty, profit)
        dif_prof = sorted(dif_prof, key=lambda x: (x[0], x[1]))
        ans = 0

        for w in worker:
            if w < dif_prof[0][0]:
                continue
            if w >= dif_prof[-1][0]:
                ans += dif_prof[-1][1]
                continue
                
            l, r = 0, len(dif_prof)
            ind = -1
            
            while l <= r:
                m = (l + r) // 2
                if dif_prof[m][0] > w:
                    ind = m
                    r = m - 1
                else:
                    l = m + 1
            # print(w, ind)
            if dif_prof[:ind]:
                ans += max([x[1] for x in dif_prof[:ind]])
        
        return ans
                
                