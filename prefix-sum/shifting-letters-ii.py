SHIFT = {0: -1, 1: 1}

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shifts_track = [0] * (n + 1)

        for st, en, di in shifts:
            shifts_track[st] += SHIFT[di]
            shifts_track[en + 1] -= SHIFT[di]

        pref_sum = list(accumulate(shifts_track))
        
        ans = ""
        for i, ch in enumerate(s):
            ans += chr((ord(ch) - ord("a") + pref_sum[i]) % 26 + ord("a") )

        return ans