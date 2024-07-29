class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        ans=0
        first=1
        second=2
        for i in range(n-2):
            ans=first+second
            first=second
            second=ans
        return ans
