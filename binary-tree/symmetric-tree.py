# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def tree_check(this, other):
            if not this and not other:
                return True
            if not this:
                return False
            if not other:
                return False

            return (this.val == other.val and
                    tree_check(this.left, other.right) and
                    tree_check(this.right, other.left))

        if not root:
            return True
        
        return tree_check(root, root)