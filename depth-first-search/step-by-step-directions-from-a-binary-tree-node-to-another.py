# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        path = []
        def transversal(node):
            nonlocal startValue, destValue, to_start, to_dest

            if not node:
                return

            if node.val == startValue:
                to_start = "".join(path)

            if node.val == destValue:
                to_dest = "".join(path)

            path.append("L")
            transversal(node.left)
            path.pop()

            path.append("R")
            is_right = transversal(node.right)
            path.pop()


        path = []
        to_start, to_dest = "", ""
        transversal(root)

        i = 0
        while i < min(len(to_start), len(to_dest)) and to_start[i] == to_dest[i]:
            i += 1
        
        return "U" * (len(to_start) - i) + to_dest[i:]

