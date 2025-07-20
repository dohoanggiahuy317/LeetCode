class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_prof = zip(difficulty, profit)
        diff_prof = sorted(diff_prof)

        prefMax = [0] * len(diff_prof)
        for i, (diff, prof) in enumerate(diff_prof):
            prefMax[i] = max(prefMax[i - 1] if i > 0 else 0, diff_prof[i][1])

        ans = 0
        for w in worker:
            l, r = 0, len(worker) - 1
            best = -1

            while l <= r:
                m = (l + r) // 2

                if w < diff_prof[m][0]:
                    r = m - 1
                else:
                    best = m
                    l = m + 1
        
            ans += prefMax[best] if best != -1 else 0

        return ans

                    