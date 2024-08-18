class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i, j = 0, 0
        
        for com in commands:
            if com == "DOWN":
                i += 1
            if com == "UP":
                i -= 1
            if com == "RIGHT":
                j += 1
            if com == "LEFT":
                j -= 1

        return i * n + j