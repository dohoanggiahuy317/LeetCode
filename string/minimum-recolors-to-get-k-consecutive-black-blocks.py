class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        swap_used = blocks[:k].count("W")
        ans = swap_used

        for r in range(k, len(blocks)):
            swap_used += int(blocks[r] != "B")

            if blocks[r - k] == "W":
                swap_used -= 1
        
            ans = min(ans, swap_used)

        return ans