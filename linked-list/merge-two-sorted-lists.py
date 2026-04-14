# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None

        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            res = list1
            res.next = self.mergeTwoLists(list1.next, list2)
        else:
            res = list2
            res.next = self.mergeTwoLists(list1, list2.next)

        return res
        