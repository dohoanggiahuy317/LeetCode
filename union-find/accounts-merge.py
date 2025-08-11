class Tree:
    def __init__(self, num_node):
        self.parents = [i for i in range(num_node)]
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.parents[yr] = xr

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        tree = Tree(len(accounts))
        
        handled_emails = defaultdict(int)
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                if (name, email) in handled_emails:
                    tree.union(i, handled_emails[(name, email)])
                else:
                    handled_emails[(name, email)] = i
        
        ans = defaultdict(list)
        for (name, email), parent in handled_emails.items():
            root = tree.find(parent)
            if root not in ans:
                ans[root] = [[name], []]
            ans[root][1].append(email)

        return [x[0] + sorted(x[1]) for x in ans.values()]

           