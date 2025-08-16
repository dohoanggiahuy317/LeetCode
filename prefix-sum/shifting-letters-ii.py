

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        track = [0] * (n+1)
        di_map = {0: -1, 1: 1}

        for start, end, di in shifts:
            track[start] += di_map[di]
            track[end + 1] -= di_map[di]

        shift_map = list(accumulate(track))
        ans = ""
        for i, ch in enumerate(s):
            ans += chr((ord(ch) + shift_map[i] - ord("a")) % 26 + ord("a"))

        return ans

        