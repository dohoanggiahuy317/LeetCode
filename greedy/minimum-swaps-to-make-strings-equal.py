class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        temp = Counter(s1 + s2)
        if not all(x % 2 == 0 for _, x in temp.items()):
            return -1

        x, y = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    x += 1
                else:
                    y += 1
        
        max_pair = max(x, y) // 2
        rest = max(x, y) - 2 * max_pair
        
        return max_pair + 2 * rest