# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(root, lvl):
            nonlocal t1, t2, x, y
            if not root:
                return
            
            if root.left and root.left.val == x:
                t1 = (root.val, lvl + 1)
            if root.right and root.right.val == x:
                t1 = (root.val, lvl + 1)
            if root.left and root.left.val == y:
                t2 = (root.val, lvl + 1)
            if root.right and root.right.val == y:
                t2 = (root.val, lvl + 1)     

            dfs(root.left, lvl + 1)
            dfs(root.right, lvl + 1)

        t1, t2 = None, None
        dfs(root, 0)

        if not t1 or not t2:
            return False

        if t1[0] == t2[0]:
            return False

        if t1[1] == t2[1]:
            return True

        return False
