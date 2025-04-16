class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        temp = "1" + s + "1"
        li_track = []


        curr_char = "1"
        track = 1
        for i in range(1, len(temp)):
            if temp[i] == curr_char:
                track += 1
            else:
                li_track.append((track, curr_char))
                curr_char = temp[i]
                track = 1

            if i == len(temp) - 1:
                li_track.append((track, curr_char))
        
        
        if len(li_track) == 1:
            return li_track[0][0] - 2
        
        start = -1
        curr_max = -float("INF")
        # print(li_track)

        for i in range(len(li_track) - 2):
            # print(i)
            if li_track[i][0] + li_track[i+1][0] + li_track[i+2][0] > curr_max and li_track[i][1] == "0":
                start = i
                curr_max = li_track[i][0] + li_track[i+1][0] + li_track[i+2][0]

        # print(start)
        if start == -1:
            return sum(list(map(int, list(s))))
        
        li_track[start] = (li_track[start][0], "1")
        li_track[start+1] = (li_track[start+1][0], "1")
        li_track[start+2] = (li_track[start+2][0], "1")

        ans = 0
        for x, y in li_track:
            if y == "1":
                ans += x

        return ans - 2