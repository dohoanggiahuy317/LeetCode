# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        stack = []
        node = head.next
        while node:
            mask = node
            node = node.next

            mask.next = None
            stack.append(mask)
            

        ans = head
        ptr = ans

        while stack:
            
            nxt = stack.pop()
            ptr.next = nxt
            ptr = ptr.next

            rev_stack = []
            while stack:
                rev_stack.append(stack.pop())
            stack = rev_stack
        
        return ans

