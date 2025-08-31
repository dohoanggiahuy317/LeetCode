class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        def dfs(node):
            cnt = Counter({labels[node]: 1})
            for neigh in graph[node]:
                cnt += dfs(neigh)
            ans[node] = cnt[labels[node]]
            return cnt

        ans = [0] * n
        dfs(0)
        
        return ans