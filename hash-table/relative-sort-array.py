class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_counter = Counter(arr1)
        ans = []

        for value in arr2:
            ans.extend([value] * arr1_counter[value])
            del arr1_counter[value]
            
        remaining = sorted(arr1_counter.elements())
        ans.extend(remaining)

        return ans