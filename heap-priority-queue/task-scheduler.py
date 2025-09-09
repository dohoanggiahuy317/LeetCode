class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        curr_time = 0
        tasks_count = Counter(tasks)
        queue = [(0, -freq, task) for task, freq in tasks_count.items()]

        while queue:
            start_time, neg_freq, task = heapq.heappop(queue)
            if start_time > curr_time:
                curr_time = start_time

            new_time = curr_time + n + 1
            
            if neg_freq + 1 != 0:
                heapq.heappush(queue, (new_time, neg_freq + 1, task))
            
            curr_time += 1

        return curr_time

