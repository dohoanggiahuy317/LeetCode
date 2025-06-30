# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        curr, prev = head, None

        while curr:
            curr = curr.next
            if cnt < n+1:
                cnt += 1

            if not prev and cnt == n+1:
                prev = head
            elif prev:
                prev = prev.next
        
        if not prev:
            return None

        prev.next = prev.next.next
        return head
            