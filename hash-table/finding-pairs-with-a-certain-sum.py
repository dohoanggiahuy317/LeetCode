class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_c = Counter(nums1)
        self.nums2_l = nums2[:]

    def add(self, index: int, val: int) -> None:
        self.nums2_l[index] += val

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.nums2_l:
            ans += self.nums1_c[tot - num]

        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)