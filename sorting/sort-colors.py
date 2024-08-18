class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq = [0] * 3

        for n in nums:
            freq[n] += 1

        idx = 0
        for i in range(len(freq)):
            for _ in range(freq[i]):
                nums[idx] = i
                idx += 1       