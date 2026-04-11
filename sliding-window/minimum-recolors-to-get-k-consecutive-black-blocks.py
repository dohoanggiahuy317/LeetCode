class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        swap_used = blocks[:k].count("W")
        ans = swap_used

        for r in range(k, len(blocks)):

            swap_used += int(blocks[r] != "B")

            if r - l + 1 > k:
                if blocks[l] == "W":
                    swap_used -= 1
                l += 1
            
            if r - l + 1 >= k:
                ans = min(ans, swap_used)

        return ans