class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): # constraint
            return False

        s2t_map = {}
        t2s_map = {}

        for char_s, char_t in zip(s, t):
            if char_t in t2s_map and t2s_map[char_t] != char_s:
                return False
            if char_s in s2t_map and s2t_map[char_s] != char_t:
                return False

            t2s_map[char_t] = char_s
            s2t_map[char_s] = char_t

        return True