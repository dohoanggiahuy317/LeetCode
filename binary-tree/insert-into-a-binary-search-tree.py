# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)

        if root.val < val:
            if root.right == None:
                root.right = TreeNode(val)
                return root
            else:
                self.insertIntoBST(root.right, val)
        else:
            if root.left == None:
                root.left = TreeNode(val)
                return root
            else:
                self.insertIntoBST(root.left, val)

        return root