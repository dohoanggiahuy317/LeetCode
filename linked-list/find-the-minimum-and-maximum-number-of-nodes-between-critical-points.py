# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr_max, curr_min = 10 ** 31, 10 ** 31
        prev = head
        curr = head.next

        temp = []
        count = 1

        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if temp:
                    curr_min = min(curr_min, count - temp[-1])
                temp.append(count)
            count += 1
            prev = curr
            curr = curr.next

        if len(temp) <= 1 or curr_min == 10 ** 31:
            return [-1, -1]

        return [curr_min, temp[-1] - temp[0]]

