class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        MAP_DIRECTION = {0: -1, 1: 1}

        N = len(s)
        changes = [0] * (N+1)
        a = ord('a')
        for start, end, shift in shifts:
            changes[start] += MAP_DIRECTION[shift]
            changes[end+1] -= MAP_DIRECTION[shift]
        ans = []
        for c, change in zip(s, accumulate(changes)):
            ans.append(chr(a + (ord(c) - a + change) % 26))
        return "".join(ans)