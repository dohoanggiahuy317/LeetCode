class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        new_arr = list(map(lambda x: x-1, nums))

        new_arr.sort()

        return max(new_arr[-1] * new_arr[-2], new_arr[0] * new_arr[1])

