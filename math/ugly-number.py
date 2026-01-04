class Solution:
    def isUgly(self, n: int) -> bool:
        def div_2(n):
            if n % 2 != 0:
                return n
            return div_2(n/2)
        
        def div_3(n):
            if n % 3 != 0:
                return n
            return div_3(n/3)
        
        def div_5(n):
            if n % 5 != 0:
                return n
            return div_5(n/5)
        
        if n == 0:
            return False
        
        new = div_2(div_3(div_5(n)))
        if new == 1:
            return True
        else:
            return False
        
        