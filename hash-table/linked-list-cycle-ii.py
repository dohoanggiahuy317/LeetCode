# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sl, fa = head, head
        while fa and fa.next:
            fa = fa.next.next
            if fa:
                sl = sl.next
            if fa == sl:
                break
        else:
            return None

        ot = head
        while ot != sl:
            sl = sl.next
            ot = ot.next

        return sl

        