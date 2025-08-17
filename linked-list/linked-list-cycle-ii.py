# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        meet = False

        while (fast or slow) and (not meet):
            if fast and fast.next:
                fast = fast.next.next
            else:
                return None
            slow = slow.next

            if fast == slow:
                meet = True

        other = head
        while other != slow:
            other = other.next
            slow = slow.next

        return slow

