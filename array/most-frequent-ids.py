class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        h = []
        d = {}
        res = []
        for i, f in zip(nums, freq):
            if i in d:
                d[i] += f
            else:
                d[i] = f

            heappush(h, [-d[i], i])
            while h and d[h[0][1]] != -h[0][0]:
                heappop(h)
            res.append(-h[0][0] if h else 0)
            # print(h)
        return res