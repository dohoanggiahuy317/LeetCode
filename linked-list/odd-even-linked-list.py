# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        head1 = head
        head2 = head1.next

        temp1 = head1
        temp2 = head2

        while temp1.next and temp2.next:
            temp1.next = temp2.next
            temp1 = temp2.next

            temp2.next = temp1.next
            temp2 = temp1.next

        temp1.next = head2

        return head