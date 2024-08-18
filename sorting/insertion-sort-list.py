# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = ListNode(0)

        while curr:
            trace = prev
            nextNode = curr.next

            while trace.next and trace.next.val < curr.val:
                trace = trace.next

            curr.next = trace.next
            trace.next = curr
            curr = nextNode

        return prev.next