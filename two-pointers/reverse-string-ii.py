class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        li_s = list(s)
        
        chunk_l, chunk_r = 0, min(k, n) - 1

        while chunk_l < len(s):
            l, r = chunk_l, min(chunk_r, n - 1)

            while l < r:
                li_s[l], li_s[r] = li_s[r], li_s[l]
                l += 1
                r -= 1
            
            chunk_l += 2 * k
            chunk_r += 2 * k

        return "".join(li_s)

