class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0

        for j, char in enumerate(typed):
            if name[i] == typed[j]:
                i += 1

            if i == len(name):
                return True
            
        return False