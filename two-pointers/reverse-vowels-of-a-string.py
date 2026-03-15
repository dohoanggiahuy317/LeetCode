class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = "AEIOUaeiou"

        l, r = 0, len(s) - 1
        li_s = list(s)
        while l < r:
            if s[l] not in VOWELS:
                l += 1
            elif s[r] not in VOWELS:
                r -= 1
            else:
                li_s[l], li_s[r] = li_s[r], li_s[l]
                r -= 1
                l += 1

        return "".join(li_s)

