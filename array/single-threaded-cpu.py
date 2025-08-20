class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # CONSTANT
        n = len(tasks)

        # Prep
        tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        tasks.sort()
    
        result = []
        pq = []
        time = 0
        i = 0
        
        # Run
        while i < n or pq:
            while i < n and tasks[i][0] <= time:
                et, pt, idx = tasks[i]
                heapq.heappush(pq, (pt, idx))
                i += 1
            
            if pq:
                pt, idx = heapq.heappop(pq)
                result.append(idx)
                time += pt
            else:
                time = tasks[i][0]
        
        return result