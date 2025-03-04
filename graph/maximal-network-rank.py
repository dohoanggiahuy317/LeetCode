
from collections import defaultdict, Counter
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        maps = defaultdict(set)

        for u, v in roads:
            maps[u].add(v)
            maps[v].add(u)

        li = list(map(lambda x: (x[0], len(x[1])), maps.items() ))
        ans = 0

        for i in range(len(li) - 1):
            c1, n1 = li[i]
            for j in range(i+1, len(li)):
                c2, n2 = li[j]

                if c2 in maps[c1] or c1 in maps[c2]:
                    ans = max(ans, n1+n2-1)
                else:
                    ans = max(ans, n1+n2)
                
        return ans


        # print(maps)
        # print(net)

        # li = sorted( list (map(lambda x: (x[0], x[1]), net.items() )), reverse=True, key=lambda x: x[1] )
    
        # c1, n1 = li[0]
        # c2, n2 = li[1]

        # print(c1, c2)

        # if c2 in maps[c1] or c1 in maps[c2]:
        #     return n1+n2-1
        # return n1+n2

