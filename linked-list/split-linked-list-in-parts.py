# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total = 0
        it = head
        while it:
            it = it.next
            total += 1

        ave = total // k
        rem = total - ave * k

        ans = []
        it = head

        for i in range(k):
            curr = ListNode()
            if it == None:
                ans.append(None)
                continue
            
            curr.next = it
            if rem > 0:
                for j in range(ave):
                    it = it.next
                rem -= 1
            else:
                for j in range(ave - 1):
                    it = it.next
            
            s = it.next
            it.next = None
            print(it)
            it = s

            ans.append(curr.next)

        return ans
