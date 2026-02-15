class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        good = []
        for offer in special:
            items, offer_price = offer[:n], offer[n]
            buy_all = sum(items[i] * price[i] for i in range(n))
            if offer_price < buy_all:
                good.append(offer)

        dp = {}

        def explore_buy(rem_needs: Tuple[int, ...]) -> int:
            if rem_needs in dp:
                return dp[rem_needs]

            best = sum(rem_needs[i] * price[i] for i in range(n))

            for offer in good:
                items, offer_price = offer[:n], offer[n]

                if all(items[i] <= rem_needs[i] for i in range(n)):
                    nxt_needs = tuple(rem_needs[i] - items[i] for i in range(n))
                    best = min(best, offer_price + explore_buy(nxt_needs))

            dp[rem_needs] = best
            return best

        return explore_buy(tuple(needs))