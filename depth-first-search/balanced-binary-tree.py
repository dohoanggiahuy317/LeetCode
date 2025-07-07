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

            height_left = height(root.left) 
            height_right = height(root.right) 
            
            diff_check = abs(height_left - height_right) <= 1
            if not diff_check and ans:
                ans = False

            return max(height_left, height_right) + 1

        height(root)
        return ans


