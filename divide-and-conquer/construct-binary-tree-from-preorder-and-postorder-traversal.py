class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        tree_map = defaultdict()
        
        while len(preorder) > 2:
            for i in range(n - 2):
                if sorted(preorder[i:i + 3]) == sorted(postorder[i:i+3]):
                    if preorder[i] not in tree_map:
                        tree_map[preorder[i]] = TreeNode(preorder[i])
                    if preorder[i+1] not in tree_map:
                        tree_map[preorder[i+1]] = TreeNode(preorder[i+1])
                    if preorder[i+2] not in tree_map:
                        tree_map[preorder[i+2]] = TreeNode(preorder[i+2])
                    
                    tree_map[preorder[i]].left = tree_map[preorder[i+1]]
                    tree_map[preorder[i]].right = tree_map[preorder[i+2]]

                    preorder.pop(i + 1)
                    preorder.pop(i + 2)

                    postorder.pop(i)
                    postorder.pop(i + 1)

        if len(preorder) == 2:
            tree_map[preorder[0]].left = tree_map[preorder[1]]

        return tree_map[preorder[0]] 






