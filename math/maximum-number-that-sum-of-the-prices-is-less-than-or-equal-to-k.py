class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
            
        def f(mid):
            s = 0
            le = len(bin(mid)[2:])

            for i in range(x - 1, le, x):
                block_size = 2 ** i
                num_block = floor((mid + 1) / block_size)

                s += (block_size) * (num_block // 2)
                if num_block % 2 == 1:
                    s  += (mid + 1) % block_size
            return s

        l = 0
        r = 10**20
        
        while l+1 < r:
            m = (l+r) // 2
            
            if f(m+1) <= k: 
                l = m 
            else: 
                r = m
                
        return l + 1