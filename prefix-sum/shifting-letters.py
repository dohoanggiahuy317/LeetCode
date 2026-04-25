class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        total = sum(shifts)
        prefix = list(accumulate(shifts))

        result = []
        for i in range(n):
            shift_amount = (total - (prefix[i - 1] if i > 0 else 0)) % 26
            new_char = chr((ord(s[i]) - ord("a") + shift_amount) % 26 + ord("a"))
            result.append(new_char)
            
        return "".join(result)