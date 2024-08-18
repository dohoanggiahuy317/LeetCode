# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        n = 0
        curr = head
        last = None
        while curr:
            n += 1
            last = curr
            curr = curr.next

        k = k%n


        if n == 1 or k == 0:
            return head

        start = head
        prev = None
        for i in range(n-k):
            prev = start
            start = start.next

        last.next = head
        prev.next = None
        return start

        