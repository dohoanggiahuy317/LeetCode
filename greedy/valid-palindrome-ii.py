class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palin_check(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                break
            l += 1
            r -= 1

        return palin_check(s, l, r - 1) or palin_check(s, l + 1, r)