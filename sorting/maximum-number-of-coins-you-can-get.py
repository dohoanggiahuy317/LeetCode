class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        ans = 0
        piles.sort()

        e = len(piles) - 1
        s = 0

        while e > s:
            ans += piles[e-1]

            s += 1
            e -= 2

        return ans
        