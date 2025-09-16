class NumArray:

    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.tree = [0] * (2 * self.N)
        self.tree[self.N:] = nums


        for i in range(self.N - 1, 0, -1):
           self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) | 1]

    def update(self, i: int, x: int) -> None:
        i += self.N
        self.tree[i] = x
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def sumRange(self, l: int, r: int) -> int:
        ans = 0
        l += self.N 
        r += self.N + 1
        while l < r:
            if (l & 1):
                ans += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                ans += self.tree[r]
                
            l >>= 1
            r >>= 1
        return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)