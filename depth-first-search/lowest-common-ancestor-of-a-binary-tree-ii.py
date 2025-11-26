# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def transversal(root):
            nonlocal condition, found
            
            if not root:
                return root

            is_left = transversal(root.left)
            is_right = transversal(root.right)

            condition = 0
            if root == p or root == q:
                condition += 1
            if is_left:
                condition += 1
            if is_right:
                condition += 1
            if condition == 2:
                found = True
            
            if (is_left and is_right) or (root == p or root == q):
                return root
            
            return is_left if is_left else is_right

        found, condition = False, 0
        ans = transversal(root)
        return ans if found else None