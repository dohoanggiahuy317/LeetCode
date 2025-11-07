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

        stack = deque()
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

            if stack:
                nxt = stack.popleft()
                ptr.next = nxt
                ptr = ptr.next
        
        return ans

