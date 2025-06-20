class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        trackUp, trackDown = [0] * len(s), [0] * len(s)

        for st, e, d in shifts:
            trackUp[e] += 2*d - 1
            trackDown[st] += 2*d - 1

        prefDown, prefUp = [0], [0]
        for i in range(len(s)):
            prefDown.append(prefDown[-1] + trackDown[len(trackDown)-1 - i])
            prefUp.append(prefUp[-1] + trackUp[len(trackUp)-1 - i])

        ans = ''
        for i in range(len(s)):
            char_shift = prefUp[len(s) - i] - prefDown[len(s) - (i+1)]
            ans +=  chr((ord(s[i]) - ord("a") + char_shift) % 26 + ord("a"))

        return ans