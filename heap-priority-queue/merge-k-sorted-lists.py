# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            
            if l1.val > l2.val:
                l2.next = merge(l1, l2.next)
                return l2
            else:
                l1.next = merge(l1.next, l2)
                return l1
        if not lists:
            return None

        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            lists.append(merge(l1, l2))

        return lists[0]