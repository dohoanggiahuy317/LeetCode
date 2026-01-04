class Solution:
    def isHappy(self, n: int) -> bool:
        def sq_sum_func(n):
            if n == 1 or n == 7:
                return True
            if n < 10:
                return False
            
            sq_sum = 0
            for i in str(n):
                sq_sum += int(i)**2
                
            return sq_sum_func(sq_sum)
        
        return sq_sum_func(n)