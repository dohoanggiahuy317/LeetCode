class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = s.lower()

        l = 0
        r = len(s) - 1

        while l < r:
            if not ns[l].isalpha() and not ns[l].isdigit():
                l += 1
                continue
            if not ns[r].isalpha() and not ns[r].isdigit():
                r -= 1
                continue

            if ns[l] != ns[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
        