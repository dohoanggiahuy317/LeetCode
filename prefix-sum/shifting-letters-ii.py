class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        map_direction = {0:-1, 1:1}
        change = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            change[start] += map_direction[direction]
            change[end + 1] -= map_direction[direction]

        ans = ""

        for char, num in zip(s, accumulate(change)):
            ans += chr((ord(char) + num - ord("a")) % 26 + ord("a"))
        
        return ans