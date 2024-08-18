# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def search(root):
            nonlocal ans
            if root == None:
                return

            search(root.left)
            ans.append(root.val)
            search(root.right)

        ans = []
        search(root)
        return ans