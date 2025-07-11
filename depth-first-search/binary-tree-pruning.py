# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def found(root):
            if not root:
                return False

            found_left = found(root.left)
            found_right = found(root.right)
            if not found_left:
                root.left = None
            if not found_right:
                root.right = None
            
            # print(root.val, found_left, found_right)
            return root.val == 1 or (found_left or found_right)

        dummy = TreeNode()
        dummy.left = root
        found(dummy)
        return dummy.left