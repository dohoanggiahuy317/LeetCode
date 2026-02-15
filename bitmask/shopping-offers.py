class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        buy_all = sum(need * price[i] for i, need in enumerate(needs))

        special = sorted(special, reverse = True, key = lambda x: x[n])
        special_idx = 0

        remain_needs = []
        cost = 0

        while special_idx < len(special):
            if all(need >= special[special_idx][i] for i, need in enumerate(needs)):
                for i, need in enumerate(needs):
                    remain_needs.append(need - special[special_idx][i])
                
                cost += special[special_idx][n]
                needs = remain_needs[:]
                remain_needs = []
            else:
                special_idx += 1


        for i, need in enumerate(needs):
            if need > 0:
                cost += need * price[i]

        return min(cost, buy_all)
