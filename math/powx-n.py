class Solution:
    def myPow(self, x: float, n: int) -> float:
        count = 1
        
        if n == 0:
            return 1
        
        if n > 0:
            res = x
            while count < n:
                res *= res
                count *= 2
                
            remainder = count - n
            for i in range(remainder):
                res /= x
            return res
            
        if n < 0:
            res = 1/x
            while count < abs(n):
                res *= res
                count *= 2
                
            remainder = count - abs(n)
            for i in range(remainder):
                res /= 1/x
            return res
        
#         return x ** n
        