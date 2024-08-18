class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x < 0:
            s = s[0] + s[1:][::-1]
        else:
            s = s[::-1]
        
        t = int(s)

        if -2**31 <= t and t < 2**31-1:
            return t
        return 0