# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        curr = head
        while curr and curr.next:
            while curr.next.val != 0:
                curr.val += curr.next.val
                curr.next = curr.next.next

            while curr.next and curr.next.val == 0:
                # if curr.next.next == None:
                #     return
                curr.next = curr.next.next
            curr = curr.next

            # print(head)
        return head
