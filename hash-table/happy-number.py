class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            temp = n
            n = 0
            
            while temp > 0:
                n += (temp % 10) ** 2
                temp //= 10
            

            

        return True