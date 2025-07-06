class Solution:

    def __init__(self, w: List[int]):
        self.pref = list(accumulate(w))

    def pickIndex(self) -> int:
        target = random.randint(1, self.pref[-1])
        return bisect_left(self.pref, target)
        # l, r = 0, len(self.pref) - 1

        # while l < r:
        #     m = (l + r) // 2
        #     if self.pref[m] < tar:
        #         l = m + 1
        #     elif self.pref[m] > tar:
        #         r = m
        #     else:
        #         return m

        # return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()