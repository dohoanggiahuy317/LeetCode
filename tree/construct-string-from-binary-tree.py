# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def trans(root):
            if root == None:
                return ""

            if root.right != None:
                return str(root.val) + "(" + trans(root.left) + ")(" + trans(root.right) + ")"  

            if root.left != None:
                return str(root.val) + "(" + trans(root.left) + ")"
            
            return str(root.val)
            

        return trans(root)