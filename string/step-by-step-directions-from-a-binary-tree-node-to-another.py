# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        

        def transversal(node):
            nonlocal startValue, destValue

            if not node:
                return None

            if node.val == startValue or node.val == destValue:
                return node

            is_left = transversal(node.left)
            is_right = transversal(node.right)

            if is_left and is_right:
                return node
            if is_left:
                return is_left
            return is_right

        lca = transversal(root)

        def find_node(node, path, f):
            if not node:
                return False, ""

            if node.val == f:
                return True, path

            left_status, left_path = find_node(node.left, path + "L", f)
            right_status, right_path = find_node(node.right, path + "R", f)
            
            if left_status:
                return left_status, left_path
            return right_status, right_path

        return "U" * len(find_node(lca, "", startValue)[1]) + find_node(lca, "", destValue)[1]

