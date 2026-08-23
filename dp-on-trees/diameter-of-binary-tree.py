# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def transversal(root):
            if not root:
                return 0, 0

            diameter_left, longest_left = transversal(root.left)
            diameter_right, longest_right = transversal(root.right)

            diameter = max(diameter_left, diameter_right, longest_left + longest_right)

            return diameter, max(longest_left, longest_right) + 1

        ans, _ = transversal(root)
        
        return ans

