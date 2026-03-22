class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        j = 0
        num_child = 0

        for child in g:
            while j < len(s) and s[j] < child:
                j += 1
            
            if j < len(s) and s[j] >= child:
                num_child += 1

        return num_child
