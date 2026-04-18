class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr_1 = Counter(arr1)
        result = []
        for num in arr2:
            result.extend([num] * arr_1[num])
            del arr_1[num]

        remain = sorted(arr_1.elements())
        result.extend(remain)
        return result
