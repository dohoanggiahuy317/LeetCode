class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def backtrack(i1, i2, i3):
            nonlocal s1, s2, s3

            if i1 == len(s1) and i2 == len(s2):
                return True

            is_s1, is_s2 = False, False

            if i1 < len(s1) and s1[i1] == s3[i3]:
                is_s1 = backtrack(i1 + 1, i2, i3 + 1)

            if i2 < len(s2) and s2[i2] == s3[i3]:
                is_s2 = backtrack(i1, i2 + 1, i3 + 1)

            return is_s1 or is_s2

        return backtrack(0, 0, 0)
            
        


            
