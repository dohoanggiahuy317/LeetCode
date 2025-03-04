# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse_sub(self, head, k):
        prev = None
        curr = head
        tail = head

        while k > 0:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
            k -= 1
        
        return prev, tail, curr

    def len(self, head):
        ans = 0
        while head:
            ans += 1
            head = head.next

        return ans

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        l = self.len(head)
        if l < k:
            return head

        num_it = l // k
        ans = None
        curr_h = head
        prev_t = None
        
        for z in range(num_it):
            curr_h, curr_t, next_h = self.reverse_sub(curr_h, k)
            if z == 0:
                ans = curr_h

            # print(curr_h)
            # print(curr_t)
            # print(next_h)
            # print(prev_t)
            # print(ans)
            # print()
            
            if prev_t:
                prev_t.next = curr_h
            curr_t.next = next_h

            prev_t = curr_t
            curr_h = next_h

            # print(curr_h)
            # print(prev_t)
            # print(ans)
            # print()
            # print()



        return ans