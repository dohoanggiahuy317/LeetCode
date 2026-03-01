class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): # constraint
            return False

        char_map = {}

        for char_s, char_t in zip(s, t):
            if char_s in char_map and char_map[char_s] != char_t:
                return False

            char_map[char_s] = char_t

        return True