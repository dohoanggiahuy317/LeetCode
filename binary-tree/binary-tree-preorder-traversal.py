# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        li = []
        def addNode(root):
            li.append(root.val)
            if root.left != None:
                addNode(root.left)
            if root.right != None:
                addNode(root.right)
        addNode(root)
        return li
        