# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        

        def transversal(node, path, target):
            nonlocal startValue, destValue

            if not node:
                return False, ""

            if node.val == target:
                return True, path

            is_left, path_left = transversal(node.left, path + "L", target)
            is_right, path_right = transversal(node.right, path + "R", target)

            if is_left:
                return is_left, path_left
            
            return is_right, path_right

        to_start = transversal(root, "", startValue)[1]
        to_dest = transversal(root, "", destValue)[1]

        i = 0
        while i < min(len(to_start), len(to_dest)) and to_start[i] == to_dest[i]:
            i += 1
        
        return "U" * (len(to_start) - i) + to_dest[i:]

