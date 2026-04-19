class NumArray:

    def __init__(self, nums: List[int]):
        self.pref_sum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.pref_sum[right] - (self.pref_sum[left - 1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)