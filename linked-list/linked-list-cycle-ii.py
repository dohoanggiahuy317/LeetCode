# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        l, r = head, head.next
        count = 0

        while (l and r) and (l != r):
            if r.next:
                r = r.next.next
            else:
                return None
            count += 1
            l = l.next

        if r == l:
            t = head

            while t != l:
                t = t.next.next
                l = l.next

            return l

        return None