class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        while True:
            if n % 3 == 0:
                n /= 3
            else:
                if n == 1:
                    return True
                
                if n % 3 == 1:
                    n -= 1
                else:
                    return False