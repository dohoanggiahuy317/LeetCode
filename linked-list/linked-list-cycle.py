# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()

        it = head

        while it:
            if it in s:
                return True
            s.add(it)
            it = it.next

        return False