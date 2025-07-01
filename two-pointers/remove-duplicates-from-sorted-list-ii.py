# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mask = ListNode(-101)
        mask.next = head

        prev, curr, nex = mask, head, head.next
        ans = ListNode(-101)
        temp = ans

        while curr:
            # print(ans)
            if prev.val != curr.val and (not nex or curr.val != nex.val):
                temp.next = curr
                temp = temp.next
            
            prev = prev.next
            curr = curr.next
            if nex:
                nex = nex.next
        return ans.next
