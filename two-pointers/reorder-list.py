# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            prev = None
            it = head
            nextnode = None

            while it:
                nextnode = it.next
                it.next = prev
                prev = it
                it = nextnode

            return prev

        if head is None:
            return None

        
        fast = head.next
        slow = head


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        rev = reverse(slow.next)
        slow.next = None

        while rev:
            h_next = head.next
            r_next = rev.next
            head.next = rev
            rev.next = h_next
            rev = r_next
            head = h_next