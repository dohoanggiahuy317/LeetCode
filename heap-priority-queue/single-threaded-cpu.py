class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = [(enq_time, proc_time, idx) for idx, (enq_time, proc_time) in enumerate(tasks)]
        tasks.sort()

        pq = []
        i = 0
        time = 0
        ans = []

        while pq or i < n:
            # Load ready task
            while i < n and tasks[i][0] <= time:
                enq_time, proc_time, idx = tasks[i]
                heapq.heappush(pq, (proc_time, idx))
                i += 1
            
            if pq:
                proc_time, idx = heapq.heappop(pq)
                ans.append(idx)
                time += proc_time # add tiem that proc the current process
            
            else: # if CPU done all task, move to next time frame
                time += tasks[i][0]

        return ans

