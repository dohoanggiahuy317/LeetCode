# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        tree_map = {}
        inorder_idx = {value: i for i, value in enumerate(inorder)}
        
        def build_tree(l, r, l1, r1): # inclusive
            print(l, r, l1, r1)
            
            if l > r:
                return None
                
                            
            node = TreeNode(preorder[l])            
            node_idx = inorder_idx[node.val]
            num_left = node_idx - l1
            num_right = r1 - node_idx
            
            
            if l + 1 < len(preorder):
                node.left = build_tree( l + 1, l + num_left, l1,            node_idx - 1)
                node.right = build_tree(l + num_left + 1, r, node_idx + 1, r1)
            
            return node
            
        root = build_tree(0, len(preorder) - 1, 0, len(preorder) - 1)
        
        return root
                
                
            