# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    allNums = 0
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.allNums = 0
        def treeNumber(root, s):
            s += str(root.val)
            
            if root.left == None and root.right == None:
                self.allNums += int(s)
                return
            
            if root.left != None:
                treeNumber(root.left, s)
            
            if root.right != None:
                treeNumber(root.right, s)
                
        treeNumber(root, "")
        return self.allNums