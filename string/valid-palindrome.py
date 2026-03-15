class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()

        l = 0
        r = len(s) - 1

        while l < r:
            if not lower_s[l].isalpha() and not lower_s[l].isdigit():
                l += 1
            elif not lower_s[r].isalpha() and not lower_s[r].isdigit():
                r -= 1
            elif lower_s[l] != lower_s[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True
        