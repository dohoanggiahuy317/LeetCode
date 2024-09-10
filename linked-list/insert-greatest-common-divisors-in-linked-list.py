# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if a % b == 0:
                return b
            if b % a == 0:
                return a

            if b > a:
                return gcd(a, b-a)
            return gcd(b, a-b)

        it = head

        while it and it.next:
            newNode = ListNode(gcd(it.val, it.next.val))
            temp = it.next
            it.next = newNode
            newNode.next = temp
            it = temp

        return head