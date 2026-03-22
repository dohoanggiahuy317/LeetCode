class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        track_vowles = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        
        prev_state = {(0, 0, 0, 0, 0): -1}
        ans = 0

        for i, ch in enumerate(s):
            if ch in track_vowles:
                track_vowles[ch] = (track_vowles[ch] + 1) % 2

            state = (
                track_vowles['a'],
                track_vowles['e'],
                track_vowles['i'],
                track_vowles['o'],
                track_vowles['u'])

            if state in prev_state:
                ans = max(ans, i - prev_state[state])
            else:
                prev_state[state] = i

        return ans