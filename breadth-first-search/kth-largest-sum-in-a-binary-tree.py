# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        # Store best k sum in pq
        def get_k_level_sum(level_sum):
            nonlocal pq, k

            if len(pq) == k and level_sum > pq[0]:
                heapq.heappop(pq)
            
            if len(pq) < k:
                heapq.heappush(pq, level_sum)
            
        # BFS each row
        def get_level_sum(root):
            queue = deque([root])
            
            while queue:
                level_sum = 0

                for _ in range(len(queue)):
                    node = queue.popleft()
                    level_sum += node.val

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                get_k_level_sum(level_sum)


        # Start
        pq = []
        get_level_sum(root)

        return pq[0] if len(pq) == k else -1