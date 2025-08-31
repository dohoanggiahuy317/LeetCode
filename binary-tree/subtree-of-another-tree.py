# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def tree_check(this, that):
            if not this and that:
                return False
            if not that and this:
                return False

            if not that and not this:
                return True
            
            return tree_check(this.left, that.left) and tree_check(this.right, that.right) and this.val == that.val

        if not root and not subRoot:
            return True
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        
        return tree_check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 