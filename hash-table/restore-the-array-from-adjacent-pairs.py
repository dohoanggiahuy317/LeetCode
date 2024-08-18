class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = {}
        ans = []

        for x, y in adjacentPairs:
            if x not in d:
                d[x] = [y]
            else:
                d[x].append(y)
            if y not in d:
                d[y] = [x]
            else:
                d[y].append(x)

        def add(ans, prev, k):
            ans.append(k)
            t = None
            for x in d[k]:
                if x != prev:
                    t = x
            if t != None:
                add(ans, k, t)

        for u, v in d.items():
            if len(v) == 1:
                add(ans, None, u)
                break

        return ans

          