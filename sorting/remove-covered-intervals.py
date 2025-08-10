class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def check_cov(i1, i2):
            if i1[0] >= i2[0] and i1[1] <= i2[1]:
                return True

            return False

        ans = 0

        for i, x in enumerate(intervals):
            for j, y in enumerate(intervals):
                if i != j:
                    if check_cov(x, y):
                        break
            else:
                ans += 1

        return ans
