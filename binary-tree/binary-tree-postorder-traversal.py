# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        def trans(root):
            nonlocal ans

            if root == None:
                return

            trans(root.left)
            trans(root.right)

            ans.append(root.val)

        ans = []

        trans(root)

        return ans