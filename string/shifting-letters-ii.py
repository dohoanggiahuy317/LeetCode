class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        track = [0] * (n+1)
        MAP = {0: -1, 1: 1}

        for st, en, di in shifts:
            track[st] += MAP[di]
            track[en+1] -= MAP[di]

        ans = ""
        
        for char, amount in zip(s, accumulate(track)) :
            ans += chr((ord(char) - ord("a") + amount) % 26 + ord("a"))


        return ans

