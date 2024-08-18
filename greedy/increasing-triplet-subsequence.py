class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        x, y = float("INF"), float("INF")

        for num in nums:
            if num <= x:
                x = num
            elif num <= y:
                y = num
            else:
                return True

        return False