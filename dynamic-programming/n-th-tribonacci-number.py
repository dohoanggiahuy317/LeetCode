class Solution:
    x = {0:0, 1:1, 2:1}
    def tribonacci(self, n: int) -> int:
        if n in self.x:
            return self.x[n]
        
        self.x[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        
        return self.x[n]