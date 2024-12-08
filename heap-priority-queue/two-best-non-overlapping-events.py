class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        events.sort(key = lambda x: x[2], reverse = True)

        ans = -1
        count = 0
        cst, cen, cval = -1, -1, -1

        for st, en, val in events:
            if not (cst <= st <= cen or cst <= en <= cen or st <= cst <= en or st <= cst <= en):
                if count == 0:
                    cst, cen, cval = st, en, val
                    ans = max(ans, cval)
                count += 1
            else:
                cst, cen, cval = st, en, val
                ans = max(ans, cval)

            if count == 2:
                return max(ans, val + cval)

        return ans
            
