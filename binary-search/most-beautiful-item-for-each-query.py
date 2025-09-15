class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # CONSTANT
        n = len(items)


        prices_beauties = sorted(items)
        pref_max_beauties = [prices_beauties[0][-1]] * n
        for i in range(1, n):
            pref_max_beauties[i] = max(pref_max_beauties[i - 1], prices_beauties[i][1])

        ans = []
        for q in queries:
            idx = bisect.bisect_left(prices_beauties, [q, inf])
            # print(q, idx)
            # if idx == n:
            if idx == 0:
                ans.append(0)
            else:
                ans.append(pref_max_beauties[idx - 1])

        return ans
        


