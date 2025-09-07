# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ans = True

        def height(root):
            nonlocal ans
            
            if not root:
                return 0
            
            if not ans:
                return 0

            height_left = height(root.left) 
            height_right = height(root.right) 
            
            if not abs(height_left - height_right) <= 1:
                ans = False
                return 0

            return max(height_left, height_right) + 1

        height(root)
        return ans


