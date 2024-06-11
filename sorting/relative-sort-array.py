class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d1 = Counter(arr1)
        ans = []

        for u in arr2:
            ans += [u] * d1[u]
            del d1[u]

        res = []
        for u, v in d1.items():
            res += [u] * v
        ans += sorted(res)

        return ans