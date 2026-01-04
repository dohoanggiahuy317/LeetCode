# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def length(listNode):
    l = 0
    while listNode != None:
        l += 1
        listNode = listNode.next
    return l

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l_a, l_b = length(headA), length(headB)
        while l_a > l_b:
            headA = headA.next
            l_a -=1
        
        while l_b > l_a:
            headB = headB.next
            l_b -=1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA 
