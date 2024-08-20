
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}

        def helper(ind, M):
            nonlocal dp, n

            if (ind, M) in dp:
                return dp[(ind, M)]

            if ind == n:
                return 0

            if ind+ M * 2 >= n:
                return sum(piles[ind:])

            res = 0
            for x in range(1, 2*M+1):
                res = max(res, sum(piles[ind:]) - helper(ind+x, max(M, x)) )

            dp[(ind, M)] = res
            return res

        helper(0, 1)

        return dp[(0, 1)]



            
