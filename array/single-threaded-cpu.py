class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((s, p, i) for i, (s, p) in enumerate(tasks))
        n, i, ctime = len(tasks), 0, 0
        pq, ans = [], []

        while len(ans) < n:
            if not pq and ctime < tasks[i][0]:
                ctime = tasks[i][0]
            while i < n and tasks[i][0] <= ctime:
                s, p, idx = tasks[i]; i += 1
                heapq.heappush(pq, (p, idx))
            p, idx = heapq.heappop(pq)
            ctime += p
            ans.append(idx)
        return ans