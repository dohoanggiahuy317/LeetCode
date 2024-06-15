import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [[capital[i], -profits[i]] for i in range(len(profits))]
        projects.sort(key = lambda x: [x[0], x[1]])
        
        heap = []

        while projects and projects[0][0] <= w:
            heapq.heappush(heap, projects.pop(0)[1])

        i = 0
        while heap and i < k:
            w -= heapq.heappop(heap)

            while projects and projects[0][0] <= w:
                heapq.heappush(heap, projects.pop(0)[1]) 

            i += 1

        # for t in range(len(profits)):
        #     heapq.heappush(heap, [-profits[t], capital[t]])

        # i = 0
        # while len(heap) > 0 and i < k:
        #     temp = []

        #     while heap:
        #         f = heapq.heappop(heap)
        #         if f[1] <= w:
        #             w += -f[0]
        #             break
        #         else:
        #             temp.append(f)
            
        #     i += 1
        #     for x in temp:
        #         heapq.heappush(heap, x)


        return w