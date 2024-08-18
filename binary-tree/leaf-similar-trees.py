# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def search(root, b):
            nonlocal s1, s2
            if root == None:
                return
            
            if root.left == root.right == None:
                if b:
                    s1.append(root.val)
                else:
                    s2.append(root.val)
                
            search(root.left, b)
            search(root.right, b)
            
        s1, s2 = [], []
        
        search(root1, True)
        search(root2, False)
        
        return s1 == s2
        
        #print(s1, s2)
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        
        return True