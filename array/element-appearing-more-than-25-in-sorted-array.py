class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = {}
        n = len(arr)

        for x in arr:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

            if d[x] > n/4:
                return x