class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x, y = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    x += 1
                else:
                    y += 1
        
        if (x + y) % 2 == 1:
            return -1
        max_pair = x // 2 + y // 2
        rest = (x + y - 2 * max_pair) // 2

        return max_pair + 2 * rest