class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appear = defaultdict(int)

        for i, num in enumerate(nums):
            if target - num in appear:
                return [i, appear[target - num]]
            appear[num] = i

        return [-1, -1]