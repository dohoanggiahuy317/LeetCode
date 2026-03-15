class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = "UEOAIueoai"

        l, r = 0, len(s) - 1
        li_s = list(s)

        while l < r:
            if li_s[l] not in VOWELS:
                l += 1
            elif li_s[r] not in VOWELS:
                r -= 1
            else:
                li_s[s], li_s[r] = li_s[r], li_s[l]
                l += 1
                r -= 1
        
        return "".join(li_s)