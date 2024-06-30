# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def check(l, r):
            if l == r == None:
                return True
            if l == None or r == None:
                return False

            if l.val != r.val:
                return False

            return check(l.right, r.left) and check(l.left, r.right)

        return check(root, root)
            