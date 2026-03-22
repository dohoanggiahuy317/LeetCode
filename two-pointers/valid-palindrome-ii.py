class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        deleted = False

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif not deleted:
                if s[l] == s[r - 1]:
                    r -= 1
                elif s[l + 1] == s[r]:
                    l += 1
                else:
                    return False

                deleted = True
            else:
                return False

        return True
                
