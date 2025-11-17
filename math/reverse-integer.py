class Solution:
    def reverse(self, x: int) -> int:
        
        sx = str(x)
        return int(sx[::-1]) if sx[0] != "-" else -int(sx[1:][::-1])