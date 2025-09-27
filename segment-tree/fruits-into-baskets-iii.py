class SegmentTree:
    def __init__(self, nums):
        self.N = len(nums)
        self.tree = [0] * (self.N * 2)
        self.tree[self.N:] = nums
        for i in range(self.N - 1, 0, -1):
            self.tree[i] = min(self.tree[i << 1], self.tree[(i << 1) | 1])
    
    def update(self, idx, val):
        idx += self.N
        self.tree[idx] = val
        while idx > 1:
            self.tree[idx >> 1] = min(self.tree[idx], self.tree[idx ^ 1])
            idx >>= 1

    def query(self, l, r):
        l += self.N
        r += self.N
        ans = inf
        while l < r:
            if l & 1:
                ans = min(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = min(ans, self.tree[r])
            
            l >>= 1
            r >>= 1

        return ans
                

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        '''
        intuition:
        - consider sorted_fruits = [(baskets[i], i), ...]
        - for fruit = f, we need to find the smallest index from j to n
        given that baskets[j] >= f
        - having the segment tree with nums is the list of i based on sorted_fruits
        then we query for (j, n) as all basket after j > than f
        '''
        
        n = len(baskets)
        sorted_baskets = sorted([(basket, i) for i, basket in enumerate(baskets)])
        tree = SegmentTree([i for _, i in sorted_baskets])
        pos = {origin_i: i for i, (_, origin_i) in enumerate(sorted_baskets)}

        ans = 0
        for f in fruits:
            idx = bisect_left(sorted_baskets, (f, -1))
            if idx == n:                
                ans += 1
                continue
            
            smallest_origin_idx = tree.query(idx, n)
            if smallest_origin_idx == inf:
                ans += 1
                continue

            tree.update(pos[smallest_origin_idx], inf)

        return ans



