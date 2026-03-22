class DSU:
    def __init__(self):
        self.parents = defaultdict(str)
        self.name = defaultdict(str)

    def add(self, email, name):
        self.parents[email] = email
        self.name[email] = name

    def find(self, x):
        if self.parents[x] != x:        
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)

        if xr == yr:
            return

        if xr > yr:
            xr, yr = yr, xr

        self.parents[yr] = self.find(xr)
        self.name[yr] = self.name[self.find(xr)]
        return 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()

        for account in accounts:
            for email in account[1:]:
                dsu.add(email, account[0])

        for account in accounts:
            for email in account[1:]:
                dsu.union(account[1], email)

        graph = defaultdict(set)

        for account in accounts:
            for email in account[1:]:
                root = dsu.find(email)
                graph[root].add(email)

        ans = []

        for root, email_set in graph.items():
            ans.append([dsu.name[root]] + sorted(list(email_set)))
        
        return ans
        