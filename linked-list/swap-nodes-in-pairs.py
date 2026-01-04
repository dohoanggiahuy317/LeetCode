# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None or head.next == None:
#             return head
        
#         def swap_node_pair(head):
            
#             #odd elements in head
#             if head.next == None:
#                 return head
            
#             head.val, head.next.val = head.next.val, head.val    
            
#             #even element in head
#             if head.next.next == None:
#                 return head
            
#             #return answer
#             return swap_node_pair(head.next.next)
        
#         swap_node_pair(head)
#         return head

        if head is not None and head.next is not None:
            head.val, head.next.val = head.next.val, head.val
            self.swapPairs(head.next.next)
        return head