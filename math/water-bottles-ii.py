class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emp = numBottles
        ex = numExchange
        drinked = numBottles

        while emp >= ex:
            # print(emp, ex, drinked)
        
            emp -= ex

            drinked += 1
            emp += 1

            ex += 1
            
        return drinked