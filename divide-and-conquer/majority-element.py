

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        n = len(nums) // 2

        for num, count in counts.items():
            if count > n:
                return num

