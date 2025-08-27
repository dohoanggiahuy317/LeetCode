class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return

        self.parents[yr] = xr
        return

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        graph = DSU(n)
        acc2idx = defaultdict(int)
        idx2name = defaultdict(str)

        for i, acc in enumerate(accounts):
            name = acc[0]
            idx2name[i] = name
            for mail in acc[1:]:
                if mail not in acc2idx:
                    acc2idx[mail] = i
                else:
                    j = acc2idx[mail]
                    graph.union(i, j)

        acc_group = defaultdict(list)
        for mail, idx in acc2idx.items():
            root = graph.find(idx)
            acc_group[root].append(mail)

        ans = []
        for root, mails in acc_group.items():
            name = idx2name[root]
            person = [name] + sorted(mails)
            ans.append(person)
        
        return ans
        