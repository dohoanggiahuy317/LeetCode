class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key=lambda x: (x[0], x[1]))
        prefMax = [0] * (len(items) + 1)
        # print(items)

        for i, it in enumerate(items):
            prefMax[i+1] = max(items[i][1], prefMax[i])
        # print(prefMax)

        ans = []

        for que in queries:
            l, r = 0, len(items) - 1
            ind = -1
            while l <= r:
                m = (l + r) // 2
                if items[m][0] > que:
                    r = m - 1
                else:
                    ind = m
                    l = m + 1
            # print(que, ind)
            ans.append(prefMax[ind+1])
            # print()

        return ans

            
            