# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def itertree(root):
            nonlocal low, high, ans
            if root == None:
                return
            
            if low <= root.val <= high:
                ans += root.val
            
            itertree(root.left)
            itertree(root.right)

        ans = 0
        itertree(root)
        return ans