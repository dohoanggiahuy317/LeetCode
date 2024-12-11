import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_backlog = []
        sell_backlog = []

        for price, amount, orderType in orders:
            if orderType == 0:
                while amount > 0 and sell_backlog:
                    if sell_backlog[0][0] <= price:
                        if amount >= sell_backlog[0][1]:
                            amount -= sell_backlog[0][1]
                            heapq.heappop(sell_backlog)
                        else:
                            sell_backlog[0][1] -= amount
                            amount = 0
                    else:
                        break

                if amount > 0:
                    heapq.heappush(buy_backlog, [-price, amount])


            if orderType == 1:
                while amount > 0 and buy_backlog:
                    if -buy_backlog[0][0] >= price:
                        if amount >= buy_backlog[0][1]:
                            amount -= buy_backlog[0][1]
                            heapq.heappop(buy_backlog)
                        else:
                            buy_backlog[0][1] -= amount
                            amount = 0
                    else:
                        break

                if amount > 0:
                    heapq.heappush(sell_backlog, [price, amount])

        print(buy_backlog)
        print(sell_backlog)

        MOD = 10 ** 9 + 7
        return (sum(list(map(lambda x: x[1], buy_backlog)))%MOD + sum(list(map(lambda x: x[1], sell_backlog)))%MOD) % MOD 