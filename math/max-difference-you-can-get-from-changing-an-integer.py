class Solution:
    def maxDiff(self, num: int) -> int:
        lnum = list(str(num))
        if len(lnum) == 1:
            return 8

        def rep(c1, c2, c3):
            if lnum[0] == c1:
                temp = 1
                while temp < len(lnum) and (lnum[temp] == c1 or lnum[temp] == c2):
                    temp += 1
                if temp < len(lnum):
                    y = lnum[temp]
                    lb = [c1 if x == y else x for x in lnum]
                    b = int("".join(lb))
                else:
                    b = num
            else:
                y = lnum[0]
                lb = [c3 if x == y else x for x in lnum]
                b = int("".join(lb))

            return b

        b = rep("0", "1", "1")
        a = rep("9", "9", "9")
    
        return a - b
