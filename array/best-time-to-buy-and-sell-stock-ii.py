class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day = 0
        ans = 0

        while day < len(prices) - 1 and prices[day] >= prices[day + 1]:
            day += 1

        end = len(prices) - 1
        while end > 0 and prices[end] <= prices[end - 1]:
            end -= 1
        
        if day >= end:
            return 0

        ans -= prices[day]
        day += 1
        buy = True
        #print("BUY", day, prices[day], ans)

        while day < end:
            if prices[day] >= prices[day - 1] and prices[day] > prices[day + 1] and buy:
                ans += prices[day]
                buy = False
                #print("SELL", day, prices[day], ans)
            if prices[day] <= prices[day - 1] and prices[day] < prices[day + 1] and not buy:
                ans -= prices[day]
                buy = True
                #print("BUY", day, prices[day], ans)
            day += 1
        
        ans += prices[end]
        print("SELL", end, prices[end], ans)
        return ans

        
