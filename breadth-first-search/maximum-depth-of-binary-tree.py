# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ans = 0

        def findHeight(root, curr):
            nonlocal ans
            if not root:
                return

            ans = max(ans, curr)

            findHeight(root.left, curr + 1)
            findHeight(root.right, curr + 1)
        
        findHeight(root, 1)

        return ans