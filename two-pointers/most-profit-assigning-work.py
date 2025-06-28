class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_prof = zip(difficulty, profit)
        diff_prof = sorted(diff_prof, key=lambda x: (x[0], x[1]))
        print(diff_prof)

        ans = 0
        for wor in worker:
            if wor < diff_prof[0][0]:
                continue

            l, r = 0, len(diff_prof) - 1
            print(wor)

            while l <= r:
                m = (l + r) // 2
                print(l, r, m)

                if wor < diff_prof[m][0]:
                    r = m-1
                else:
                    l = m + 1
                
            ans += diff_prof[r][1]
            print(diff_prof[r])
            print()
        
        return ans
                
                