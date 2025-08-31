class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            cnt = Counter({labels[node]: 1})
            for neigh in graph[node]:
                if neigh != parent:
                    cnt += dfs(neigh, node)
            ans[node] = cnt[labels[node]]
            return cnt

        ans = [0] * n
        dfs(0, -1)
        
        return ans