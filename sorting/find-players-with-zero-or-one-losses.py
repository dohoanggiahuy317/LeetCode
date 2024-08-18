class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}

        for x, y in matches:
            if x not in d:
                d[x] = 0
            if y not in d:
                d[y] = 0

            d[y] += 1


        w = []
        l = []

        for pl, st in d.items():
            if st == 0:
                w.append(pl)
            if st == 1:
                l.append(pl)

        return [sorted(w), sorted(l)]
