class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        curr = int(s, 2)
        count = 0
        
        for i, num in enumerate(s):
            if num == "1":
                curr -= 2 ** (len(s) - 1 - i)
                count += 1

            if curr <= k:
                return len(s) - count

        
        return 0