class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_palindrome(s, l, r, deleted):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                elif not deleted:
                    if check_palindrome(s, l + 1, r, True) or check_palindrome(s, l, r - 1, True):
                        return True
                    return False
                else:
                    return False

            return True

        return check_palindrome(s, 0, len(s) - 1, False)
                
