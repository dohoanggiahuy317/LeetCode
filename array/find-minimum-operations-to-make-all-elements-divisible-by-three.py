class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([(0 if num % 3 == 0 else 1) for num in nums])