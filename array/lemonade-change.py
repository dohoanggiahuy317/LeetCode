class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        obtain_5, obtain_10 = 0, 0

        for bill in bills:
            if bill == 5:
                obtain_5 += 1
            elif bill == 10:
                if obtain_5 >= 1:
                    obtain_5 -= 1
                else:
                    return False
                obtain_10 += 1
            else:
                if obtain_10 >= 1 and obtain_5 >= 1:
                    obtain_5 -= 1
                    obtain_10 -= 1
                elif obtain_5 >= 3:
                    obtain_5 -= 3
                else:
                    return False

        return True

