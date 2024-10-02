class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(list(set(sorted(arr))))
        r = 1
        d = {}

        for x in temp:
            d[x] = r
            r += 1
        
        # print(d)
        ans = []

        for x in arr:
            ans.append(d[x])

        return ans