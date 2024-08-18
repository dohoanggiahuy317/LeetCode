# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ite = head
        total = 0

        while ite != None:
            total += 1
            ite = ite.next

        if n == total:
            return head.next

        ite = head
        for i in range(total - n - 1):
            ite = ite.next

        ite.next = ite.next.next
        return head
        