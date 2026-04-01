class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0
        count_cookies = 0
        
        s.sort()
        g.sort()

        for j in range(len(s)):               
            if i < len(g) and s[j] >= g[i]:
                count_cookies += 1
                i += 1
            
        return count_cookies