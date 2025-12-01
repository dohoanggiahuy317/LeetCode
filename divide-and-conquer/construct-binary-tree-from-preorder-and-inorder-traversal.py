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
        # print(inorder_idx)
        
        i = 0
        jump = 1
        
        while i < len(preorder):
            
            node_val = preorder[i]
            node_idx = inorder_idx[node_val]
            if node_val not in tree_map:
                tree_map[node_val] = TreeNode(node_val)
                
            if i + 1 < len(preorder):
                child = preorder[i + 1]
                if child not in tree_map:
                    tree_map[child] = TreeNode(child)
                
                child_idx = inorder_idx[child]
                
                if child_idx < node_idx:
                    tree_map[node_val].left = tree_map[child]
                elif child_idx > node_idx:
                    tree_map[node_val].right = tree_map[child]
                
                jump = 1
                # print(tree_map[preorder[0]])
                    
            if i + 2 < len(preorder):
                next_child = preorder[i + 2]
                if next_child not in tree_map:
                    tree_map[next_child] = TreeNode(next_child)
                
                next_child_idx = inorder_idx[next_child]
                
                if child_idx < node_idx and next_child_idx < node_idx:
                    jump = 1
                elif child_idx > node_idx and next_child_idx > node_idx:
                    jump = 1
                else:
                    tree_map[node_val].right = tree_map[next_child]
                    jump = 2
                    
            i += jump
            
        return tree_map[preorder[0]]
                
                
            