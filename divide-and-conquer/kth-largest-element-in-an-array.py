class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1

        pq = [-num for num in nums]
        heapq.heapify(pq)

        ans = 0
        for _ in range(k):
            ans = -heapq.heappop(pq)

        return ans