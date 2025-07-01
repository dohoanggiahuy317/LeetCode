# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l, r = head, head.next

        while (l and r) and (l != r):
            if r.next:
                r = r.next.next
            else:
                return False
            l = l.next

        return r == l