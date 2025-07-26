# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        tree_map = defaultdict(list)
        l, r = 0, 0

        def dfs(x, y, root):
            nonlocal tree_map, l, r
            if not root:
                return
            
            l = min(l, y)
            r = max(r, y)

            tree_map[y].append((x, root.val))
            dfs(x+1, y-1, root.left)
            dfs(x+1, y+1, root.right)

        dfs(0, 0, root)
        ans = []
        for k in range(l, r + 1):
            it = tree_map[k]
            ans.append([x[1] for x in sorted(it)])

        return ans

            