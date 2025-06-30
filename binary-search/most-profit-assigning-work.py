class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dif_prof = zip(difficulty, profit)
        dif_prof = sorted(dif_prof, key=lambda x: (x[0], x[1]))
        ans = 0
        # print(dif_prof)
        mi, ma = min(difficulty), max(difficulty)
        maprof = max(profit)

        for w in worker:
            if w <mi:
                continue
            if w >= ma:
                ans += maprof
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
                
                