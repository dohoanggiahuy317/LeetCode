# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    qFound, pFound = False, False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            nonlocal found
            if not node:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)

            condition = 0
            if node in (p, q):
                condition +=1
            if left:
                condition += 1
            if right:
                condition += 1
            if condition == 2:
                found = True
            
            if (left and right) or (node in (p, q)):
                return node
            
            return left if left else right
        
        found = False
        ans = dfs(root)
        return ans if found else None