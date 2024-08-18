# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        tr = head

        while tr != None:
            tr = tr.next
            l += 1

        tr = head
        for i in range((l+2)//2 - 1):
            tr = tr.next

        return tr