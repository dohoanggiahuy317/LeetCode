class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        cnt = Counter(nums)

        queue = []

        for elem, freq in cnt.items():
            if len(queue) < k:
                heapq.heappush(queue, (freq, elem))
            elif queue[0][0] < freq:
                heapq.heappop(queue)
                heapq.heappush(queue, (freq, elem))

        return [elem for _, elem in queue]

        