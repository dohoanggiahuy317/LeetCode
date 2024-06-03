# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i1 = ''
        s1 = l1
        while s1 != None:
            i1 += str(s1.val)
            s1 = s1.next

        i2 = ''
        s2 = l2
        while s2 != None:
            i2 += str(s2.val)
            s2 = s2.next
        
        anss = str(int(i1[::-1]) + int(i2[::-1]))[::-1]

        ans = ListNode()
        t = ans


        for i in range(len(anss)):
            if i < len(anss) - 1:
            # print(x)
                t.val = anss[i]
                t.next = ListNode()
                t = t.next
            else:
                t.val = anss[i]

        return ans