class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = set()
        cur_x = 0
        cur_y = 0

        pos.add((0, 0))

        for di in path:
            if di == "N":
                cur_y += 1
            if di == "S":
                cur_y -= 1
            if di == "E":
                cur_x += 1
            if di == "W":
                cur_x -= 1

            if (cur_x, cur_y) in pos:
                return True
            
            pos.add((cur_x, cur_y))

        return False