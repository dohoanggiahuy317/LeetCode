class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}

        for x in arr:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1


        return len(list(d.values())) == len(set(d.values()))