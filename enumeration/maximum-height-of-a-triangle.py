import math
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        maxblue1 = int(math.sqrt(blue * 4)) - 1
        maxred1 = int(math.sqrt(red * 4 + 1)) - 1 

        maxblue2 = int(math.sqrt(blue * 4 + 1)) - 1
        maxred2 = int(math.sqrt(red * 4)) - 1   

        if maxred1 % 2 != 0:
            maxred1 -= 1
        if maxblue2 % 2 != 0:
            maxblue2 -= 1

        if maxred2 % 2 == 0:
            maxred2 -= 1
        if maxblue1 % 2 == 0:
            maxblue1 -= 1

        
        return max (
                min(maxred1 + 1, maxblue1 + 1), 
                min(maxred2 + 1, maxblue2 + 1)
        )