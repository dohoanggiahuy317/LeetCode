# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree_map = defaultdict(list)
        left, right = 0, 0

        def dfs(root, x, y):
            nonlocal tree_map, left, right
            if not root:
                return
            
            # left = min(left, y)
            # right = max(right, y)

            dfs(root.left, x + 1, y-1)
            tree_map[y].append((x, root.val))
            dfs(root.right, x + 1, y+1)
        
        dfs(root, 0, 0)
        ans = []

        # print(tree_map)

        for coor, subrow in list(tree_map.items()):
            y = coor
            ans.append([x[1] for x in sorted(subrow)])
            # print(subrow)

        return ans


        

            