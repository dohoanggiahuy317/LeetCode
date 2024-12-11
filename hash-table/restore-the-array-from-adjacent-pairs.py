from collections import Counter, defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        appeared = set()
        freq = Counter()
        neigh = defaultdict(list)

        for u, v in adjacentPairs:
            neigh[u].append(v)
            neigh[v].append(u)
            freq[u] += 1
            freq[v] += 1

        start = -1
        ans = []
        for k, v in freq.items():
            if v == 1:
                start = k
                break

        ans.append(start)
        appeared.add(start)

        for i in range(len(adjacentPairs)):
            if len(neigh[start]) == 1:
                ne = neigh[start][0]
            else:
                ne = neigh[start][0] if neigh[start][0] not in appeared else neigh[start][1]
            
            ans.append(ne)
            appeared.add(ne)
            start = ne

        return ans

