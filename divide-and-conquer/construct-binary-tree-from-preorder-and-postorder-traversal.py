class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        tree_map = defaultdict()
        
        while len(preorder) > 2:
            b = True
            
            for i in range(n - 2):
                for j in range(n - 2):
                    if Counter(preorder[i:i + 3]) == Counter(postorder[j:j+3]):
                        if preorder[i] not in tree_map:
                            tree_map[preorder[i]] = TreeNode(preorder[i])
                        if preorder[i+1] not in tree_map:
                            tree_map[preorder[i+1]] = TreeNode(preorder[i+1])
                        if preorder[i+2] not in tree_map:
                            tree_map[preorder[i+2]] = TreeNode(preorder[i+2])
                        
                        tree_map[preorder[i]].left = tree_map[preorder[i+1]]
                        tree_map[preorder[i]].right = tree_map[preorder[i+2]]
                        # print(preorder, postorder)
                        preorder.pop(i + 2)
                        preorder.pop(i + 1)

                        postorder.pop(j + 1)
                        postorder.pop(j)
                        
                        b = False
                        break
                        
                if not b:
                    break

        if len(preorder) == 2:
            if preorder[0] not in tree_map:
                tree_map[preorder[0]] = TreeNode(preorder[0])
            if preorder[1] not in tree_map:
                tree_map[preorder[1]] = TreeNode(preorder[1])
            tree_map[preorder[0]].left = tree_map[preorder[1]]
        
        if preorder[0] not in tree_map:
            tree_map[preorder[0]] = TreeNode(preorder[0])

        return tree_map[preorder[0]] 






