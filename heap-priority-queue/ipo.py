import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [[capital[i], -profits[i]] for i in range(len(profits))]
        projects.sort(key = lambda x: [x[0], x[1]])
        
        heap = [0]
        i = -1
        while heap and i < k:
            w -= heapq.heappop(heap)

            while projects and projects[0][0] <= w:
                heapq.heappush(heap, projects.pop(0)[1]) 

            i += 1

        return w