# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def parsing_node(curr_path, root):
            nonlocal ans
            
            if not root.left and not root.right:
                ans.append(curr_path)
            
            if root.left:
                parsing_node(curr_path + "->" + str(root.left.val), root.left)
            if root.right:
                parsing_node(curr_path + "->" + str(root.right.val), root.right)


        ans = []
        parsing_node(str(root.val), root)
        return ans