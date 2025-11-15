# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def get_val(val, carry):
            if val >= 10:
                val %= 10
                carry = 1
            else:
                carry = 0

            return val, carry

        ptr = ListNode()
        temp = ptr
        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry
            val, carry = get_val(val, carry)

            ptr.next = ListNode(val)
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry
            val, carry = get_val(val, carry)
            ptr.next = ListNode(val)
            l1 = l1.next
            ptr = ptr.next
        
        while l2:
            val = l2.val + carry
            val, carry = get_val(val, carry)
            ptr.next = ListNode(val)
            l2 = l2.next
            ptr = ptr.next

        if carry == 1:
            ptr.next = ListNode(1)


        return temp.next
