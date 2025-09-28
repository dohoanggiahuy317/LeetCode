class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_c = Counter(nums1)
        self.nums2 = nums2[:]
        self.nums2_c = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.nums2_c[old_val] -= 1  

        self.nums2[index] += val
        
        new_val = self.nums2[index]
        self.nums2_c[new_val] += 1  

    def count(self, tot: int) -> int:
        ans = 0
        for num, freq in self.nums1_c.items():
            ans += self.nums2_c[tot - num] * freq

        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)