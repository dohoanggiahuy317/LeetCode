class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        MOST_SIG_POWER = 2 ** (k - 1)
        BASE = 2
        
        window_val = 0
        for bit in s[:k]:
            window_val = window_val * 2 + int(bit)

        visited = set([window_val])

        for r in range(k, len(s)):
            most_sig = int(s[r - k])
            bit = int(s[r])

            window_val -= most_sig * MOST_SIG_POWER
            window_val = window_val * BASE + bit

            visited.add(window_val)

        return len(visited) == (2 ** k)