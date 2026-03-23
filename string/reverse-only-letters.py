class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        li = list(s)

        while l < r:
            if not li[l].isalpha():
                l += 1
            elif not li[r].isalpha():
                r -= 1
            else:
                li[l], li[r] = li[r], li[l]
                l += 1
                r -= 1

        return "".join(li)
            