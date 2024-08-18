class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        curr = 0

        for child in g:
            if curr < len(s) and s[curr] >= child:
                curr += 1

        return curr 