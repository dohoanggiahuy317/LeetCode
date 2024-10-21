class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def split(ind, curr):
            nonlocal s, ans

            if ind >= len(s):
                # print(curr)
                ans = max(ans, len(curr))
                return curr
            
            for n in range(ind + 1, len(s) + 1):
                if s[ind:n] in curr:
                    continue
                else:
                    curr.add( s[ind:n] )
                    split(n, curr)
                    curr.remove( s[ind:n] )

        l = set()
        ans = 0
        split(0, l)
        return ans