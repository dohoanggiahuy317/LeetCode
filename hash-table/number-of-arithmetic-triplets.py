class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        snums = set(nums)
        triplet = 0

        for num in nums:
            triplet += int(num + diff in snums and num - diff in snums)

        return triplet 