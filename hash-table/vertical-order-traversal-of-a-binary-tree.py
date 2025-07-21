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

        def dfs(root, y):
            nonlocal tree_map, left, right
            if not root:
                return
            
            left = min(left, y)
            right = max(right, y)

            tree_map[y].append(root.val)
            dfs(root.left, y-1)
            dfs(root.right, y+1)

        
        dfs(root, 0)
        ans = [[] for _ in range(right - left + 1)]

        for coor, subrow in list(tree_map.items()):
            y = coor
            pos = y - left
            ans[pos] += sorted(subrow)
            # print(subrow)

        return ans


        

            