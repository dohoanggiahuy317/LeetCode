# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ite = list1

        for i in range(a-1):
            ite = ite.next

        ite2 = list1

        for i in range(b+1):
            ite2 = ite2.next

        ite.next = list2
        
        while ite.next:
            ite = ite.next

        ite.next = ite2

        return list1