"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if root == None:
            return []

        ans = []

        for x in root.children:
            ans += self.postorder(x)
        
        return ans + [root.val]