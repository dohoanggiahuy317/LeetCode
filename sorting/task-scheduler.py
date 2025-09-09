class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        curr_time = 0
        tasks_count = Counter(tasks)
        pending = [] # -> time, -freq, task
        ready = [] # -freq, task
        for task, freq in tasks_count.items():
            heapq.heappush(ready, (-freq, task))

        while ready or pending:
            
            while pending and pending[0][0] <= curr_time:
                _, neg_freq, task = heapq.heappop(pending)
                heapq.heappush(ready, (neg_freq, task))
            
            if pending and not ready:
                curr_time, neg_freq, task = heapq.heappop(pending)
                heapq.heappush(ready, (neg_freq, task))
            
            neg_freq, task = heapq.heappop(ready)
            new_time = curr_time + n + 1
            if neg_freq + 1 != 0:
                heapq.heappush(pending, (new_time, neg_freq + 1, task))
            
            curr_time += 1

        return curr_time

