class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        s = True

        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            s = not s

        if s:
            return "Bob"
        return "Alice"