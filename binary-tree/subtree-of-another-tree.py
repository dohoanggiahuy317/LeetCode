# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def treecomp(root1, root2):
            if (root1 == None and root2 != None) or (root1 != None and root2 == None ):
                return False

            if root1 == root2 == None:
                return True

            if root1.val != root2.val:
                return False

            return treecomp(root1.left, root2.left) and treecomp(root1.right, root2.right)

        if root == None and subRoot == None:
            return True
        if root == None:
            return False

        if treecomp(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)