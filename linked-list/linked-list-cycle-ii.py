# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        l, r = head, head
        b = True

        while (l and r) and (l != r or b):
            b = False
            if r.next:
                r = r.next.next
            else:
                return None
            l = l.next

# t+1 = nonloop + stloop
# 2t+1 = nonloop + 2stloop + edloop

# -> t = stloop + edloop
# nonloop = edloop - 1

        if r == l:
            t = head

            while t != l:
                t = t.next
                l = l.next

            return l

        return None