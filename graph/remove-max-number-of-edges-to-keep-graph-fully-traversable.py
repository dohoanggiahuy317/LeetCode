class Disjoint:
    def __init__(self, n):
        self.rank = [1]*n
        self.parents = [i for i in range(n)]
    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    def union(self, u, v):
        uset = self.find(u)
        vset = self.find(v)

        if uset == vset:
            return 
        if self.rank[uset] < self.rank[vset]:
            self.parents[uset] = vset
        elif self.rank[vset] < self.rank[uset]:
            self.parents[vset] = uset
        else:
            self.parents[vset] = uset
            self.rank[uset] += 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges3 = []
        wt1, wt2 = 0, 0
        ans1 = []
        ans2 = []
        ds1 = Disjoint(n+1)
        ds2 = Disjoint(n+1)
        for t, i,j in edges:
            if t==3:
                edges3.append((i,j))
        edges3.sort()        
        for i, j in edges3:
            ii = ds1.find(i)
            jj = ds1.find(j)
            if ii != jj:
                wt1 += 1
                ans1.append((3,i,j))
                ds1.union(i,j)
        for i, j in edges3:
            ii = ds2.find(i)
            jj = ds2.find(j)
            if ii != jj:
                wt2 += 1
                ans2.append((3,i,j))
                ds2.union(i,j)                


        for typee, i, j in edges:
            if typee == 1 or typee==3:
                ii = ds1.find(i)
                jj = ds1.find(j)
                if ii != jj:
                    wt1 += 1
                    ans1.append((typee,i,j))
                    ds1.union(i,j)
            if typee == 2 or typee == 3:
                ii = ds2.find(i)
                jj = ds2.find(j)
                if ii != jj:
                    wt2 +=1
                    ans2.append((typee,i,j))
                    ds2.union(i,j)
        #print(wt1, wt2)            
        if wt1 != n-1 or wt2 != n-1:
            return -1
        #print(ans1)
        #print(ans2)        
        a = set(ans1)
        for it in ans2:
            a.add(it)
        return len(edges) - len(a)                    



        