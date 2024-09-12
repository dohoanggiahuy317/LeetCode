class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bs = bin(start)[2:]
        bg = bin(goal)[2:]

        bs = "0" * (max(len(bs), len(bg)) - len(bs)) + bs
        bg = "0" * (max(len(bs), len(bg)) - len(bg)) + bg

        c = 0

        # print(bs, bg)

        for i in range(len(bs)):
            if bs[i] != bg[i]:
                c += 1
    
        return c