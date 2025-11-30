class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        

        def can_distribute(t):
            nonlocal n

            cnt = 0

            for q in quantities:
                cnt += math.ceil(q / t)

            return cnt <= n

        l, r = 1, max(quantities)
        ans = inf

        while l <= r:
            m = (l + r) >> 1
            if can_distribute(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans