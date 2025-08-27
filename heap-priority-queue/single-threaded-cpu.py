class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # sort lại task
        tasks = sorted([(start, proc, idx) for idx, (start, proc) in enumerate(tasks)])

        ready_idx, n = 0, len(tasks)
        ctime = 0
        ready_queue, ans = [], []

        while ready_queue or ready_idx < n:
            if not ready_queue and ctime < tasks[ready_idx][0]:
                ctime = tasks[ready_idx][0]

            # add tất cả các thằng ready vào queue
            while ready_idx < n and tasks[ready_idx][0] <= ctime:
                start, proc, idx = tasks[ready_idx]
                ready_idx += 1

                heapq.heappush(ready_queue, (proc, idx))

            proc, idx = heapq.heappop(ready_queue)
            ans.append(idx)
            ctime += proc

        return ans


        