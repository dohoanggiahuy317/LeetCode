# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def transverse(root):
            nonlocal d, ans
            if root == None:
                return

            if root.val in d:
                d[root.val] += 1
            else:
                d[root.val] = 1

            if root.left == None and root.right == None:
                t = 0
                for x in d.values():
                    if x % 2 == 1:
                        t += 1
                    if t > 1:
                        break
                
                if t <= 1:
                    ans += 1
            
            transverse(root.left)
            transverse(root.right)

            d[root.val] -= 1

        d = {}
        ans = 0
        transverse(root)
        return ans
