# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def split(head):
            sl, fa = head, head

            while fa and fa.next:
                fa = fa.next.next
                if fa:
                    sl = sl.next

            half = sl.next
            sl.next = None
            return half

        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1

            if l1.val > l2.val:
                l2.next = merge(l1, l2.next)
                return l2
            else:
                l1.next = merge(l1.next, l2)
                return l1
        
        if not head or not head.next:
            return head

        half = split(head)
        head = self.sortList(head)
        half = self.sortList(half)

        return merge(head, half)