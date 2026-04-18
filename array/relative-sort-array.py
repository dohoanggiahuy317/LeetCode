class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_c = Counter(arr1)
        result = []
        for num in arr2:
            result.extend([num] * arr1_c[num])
            del arr1_c[num]

        remain = sorted(arr1_c.elements())
        result.extend(remain)
        return result
