import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = defaultdict(list)

        for u, v, val in roads:
            m[u].append((val, v))
            m[v].append((val, u))
        
        ans = 0
        nodes = [float("INF")] * n
        visited = [False] * n
        tonodes = [100] * n
        tonodes[0] = 1
        nodes[0] = 0
        q = [(0, 0)]

        while q:
            dist, curr = heapq.heappop(q)
            # print(curr)
            # print(nodes)
            if visited[curr]:
                continue
            visited[curr] = True
            for val, neigh in m[curr]:
                if not visited[neigh]:
                    if nodes[neigh] == nodes[curr] + val:
                        tonodes[neigh] = (tonodes[neigh] + tonodes[curr]) % MOD

                    if nodes[neigh] > nodes[curr] + val:
                        tonodes[neigh] = tonodes[curr] % MOD
                        nodes[neigh] = nodes[curr] + val
                        heapq.heappush(q, (nodes[neigh], neigh))
            # print(nodes)
            # print(tonodes)
                
        return tonodes[n-1] % MOD


    # 0 --- 4
    # |       \ 
    # 1 --- 2--3