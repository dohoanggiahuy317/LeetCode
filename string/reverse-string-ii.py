class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        start = 0
        end = k-1
        bo = True

        while bo:
            if start >= len(s):
                bo = False
                break
            elif end >= len(s):
                end = len(s) - 1
            
            l = start
            r = end

            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            
            end += 2*k
            start += 2*k
        
        return "".join(s)

