class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0
        prev = -1

        for i in range(len(s1)):
            if c > 2:
                return False

            if s1[i] != s2[i]:
                c += 1

                if c == 1:
                    prev = i
                elif c == 2:
                    if s1[prev] != s2[i] or s1[i] != s2[prev]:
                        return False

        return c % 2 == 0

        