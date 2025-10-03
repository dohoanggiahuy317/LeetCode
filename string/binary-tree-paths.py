# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []

        def dfs(root, curr):
            nonlocal ans

            curr.append(root.val)

            if not root.left and not root.right:
                ans.append(curr[:])
            
            if root.left:
                dfs(root.left, curr)
            if root.right:
                dfs(root.right, curr)
            
            curr.pop()

        dfs(root, [])

        return [ "->".join(list(map(str, path))) for path in ans ]
