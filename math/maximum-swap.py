class Solution:
    def maximumSwap(self, num: int) -> int:
        l = list(str(num))

        ld = {int(d): i for i, d in enumerate(l)}

        for i, digit in enumerate(l):
            for j in range(9, int(i), -1):
                if j in ld and ld[j] > i:
                    l[i], l[ld[j]] = l[ld[j]], l[i]
                    return int("".join(l))

        return num