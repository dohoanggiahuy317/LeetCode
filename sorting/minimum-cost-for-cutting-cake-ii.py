import heapq

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Convert to min-heap
        horizontalCut = [-cost for cost in horizontalCut]
        verticalCut = [-cost for cost in verticalCut]
        heapq.heapify(horizontalCut)
        heapq.heapify(verticalCut)
        
        hori, ver = 1, 1
        ans = 0

        while horizontalCut and verticalCut:
            # print(ans, horizontalCut, verticalCut)
            if -horizontalCut[0] > -verticalCut[0]:
                ans -= heapq.heappop(horizontalCut) * ver
                hori += 1
            else:
                ans -= heapq.heappop(verticalCut) * hori
                ver += 1

        while horizontalCut:
            ans -= heapq.heappop(horizontalCut) * ver
        while verticalCut:
            ans -= heapq.heappop(verticalCut) * hori

        return ans
