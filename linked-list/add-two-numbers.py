# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mask = ListNode()
        curr = mask

        head1, head2 = l1, l2
        rem = 0
        while head1 and head2:
            val = head1.val + head2.val + rem
            rem = 1 if val >= 10 else 0
            val %= 10

            curr.next = ListNode(val)
            curr = curr.next
            head1 = head1.next
            head2 = head2.next

        while head1:
            val = head1.val + rem
            rem = 1 if val >= 10 else 0
            val %= 10

            curr.next = ListNode(val)
            curr = curr.next
            head1 = head1.next
        while head2:
            val = head2.val + rem
            rem = 1 if val >= 10 else 0
            val %= 10

            curr.next = ListNode(val)
            curr = curr.next
            head2 = head2.next

        if rem == 1:
            curr.next = ListNode(1)

        return mask.next
        