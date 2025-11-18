# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        queue = []

        for i, li in enumerate(lists):
            if li:
                heapq.heappush(queue, (li.val, i))

        ans = ListNode()
        ptr = ans

        while queue:
            node_val, node_idx = heapq.heappop(queue)
            node = lists[node_idx]

            ptr.next = node
            ptr = ptr.next

            node = node.next
            lists[node_idx] = node
            if lists[node_idx]:
                heapq.heappush(queue, (node.val, node_idx))


        return ans.next
        