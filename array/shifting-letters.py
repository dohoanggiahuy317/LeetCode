class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # compute sum array
        curSum = 0
        for i in range(len(shifts)-1, -1, -1):
            curSum += shifts[i]
            shifts[i] = curSum

        ans = ""

        # character replacement
        for c, shift_amt in zip(list(s), shifts):
            new_ord = ord(c) + shift_amt
            new_ord = (new_ord - ord("a")) % 26 + ord("a")
        
            ans += chr(new_ord)

        return ans

                