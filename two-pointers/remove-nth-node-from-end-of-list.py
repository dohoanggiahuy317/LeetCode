# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        mask = ListNode()
        mask.next = head

        prev, after = mask, head

        for _ in range(n):
            after = after.next

        while after:
            prev = prev.next
            after = after.next

        prev.next = prev.next.next
        return mask.next