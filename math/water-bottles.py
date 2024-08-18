class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles >= numExchange:
            # print(numBottles, ans)
            ans += numExchange
            numBottles -= numExchange - 1

        return ans + numBottles
