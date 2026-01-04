class Solution:
    def addDigits(self, num: int) -> int:      
        def sum_digi(n):
            if len(str(n)) == 1:
                return n
            
            return sum_digi(sum([int(i) for i in str(n)]))
        
        return sum_digi(num)