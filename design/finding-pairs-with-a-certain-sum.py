class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = Counter(nums1)
        self.n2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        oldval = self.nums2[index]
        newval = oldval + val

        self.n2[oldval] -= 1
        if self.n2[oldval] <= 0:
            del self.n2[oldval]
        
        if newval in self.n2:
            self.n2[newval] += 1
        else:
            self.n2[newval] = 1
        
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        ans = 0

        for x, f in self.n1.items():
            ans += f * self.n2[tot-x]

        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)