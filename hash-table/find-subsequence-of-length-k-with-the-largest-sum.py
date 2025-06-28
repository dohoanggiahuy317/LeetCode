class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nnums = [(num, i) for i, num in enumerate(nums)]
        nnums = sorted(nnums)[-k:]
        return list(map(lambda x: x[0], sorted(nnums, key=lambda x: x[1])))
