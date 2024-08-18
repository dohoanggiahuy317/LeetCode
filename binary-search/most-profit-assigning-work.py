import heapq
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse = True)

        heap = []

        for i in range(len(profit)):
            heapq.heappush(heap, [-profit[i], difficulty[i]])

        ans = 0
        diff = [0, 999999]

        for i in range(len(worker)):
            while heap and diff[1] > worker[i]:
                diff = heapq.heappop(heap)
            if diff[1] <= worker[i]:
                ans -= diff[0]

        return ans

        