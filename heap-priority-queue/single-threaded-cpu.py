class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([s, p, idx] for idx, (s, p) in enumerate(tasks))
        
        s0, p0, idx0 = tasks.pop(0)
        pq = [(p0, idx0, s0)] # -> (proc, idx, start)
        
        ans = []
        # print(tasks)
        # print(pq)
        # print(ans)
        # print()


        # keep add when pq or task have smth
        while pq or tasks:

            # lấy ra 1 thằng task
            if pq:
                p, idx, s = heapq.heappop(pq)
                ctime = s + p
                ans.append(idx)

            # add all task mà start time < cur_time:
            while tasks and tasks[0][0] <= ctime:
                ns, np, nidx = tasks.pop(0)
                heapq.heappush(pq, (np, nidx, ns))

            if tasks and not pq:
                ns, np, nidx = task.pop(0)
                pq = [(np, nidx, ns)]

            # print(tasks)
            # print(pq)
            # print(ans)
            # print()

        return ans