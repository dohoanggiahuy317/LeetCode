# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def transversal(root):
            if not root:
                return True, inf, -inf

            valid_left, min_left, max_left = transversal(root.left)
            valid_right, min_right, max_right = transversal(root.right)

            # print(root.val, valid_left, valid_right, max_left, min_right)

            return (max_left < root.val < min_right and valid_left and valid_right, 
                    min_left if root.left else root.val, 
                    max_right if root.right else root.val)

        
        return transversal(root)[0]