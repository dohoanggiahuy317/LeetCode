# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        it = head
        nextnode = None
        while it:
            nextnode = it.next
            it.next = ans
            ans = it
            it = nextnode

        return ans
