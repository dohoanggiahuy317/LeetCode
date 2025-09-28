class SegmentTree:
   def __init__(self, nums):
       self.N = len(nums)
       self.tree = [0] * (2 * self.N)
       self.tree[self.N:] = nums


       for i in range(self.N - 1, 0, -1):
           # i << 1 = i * 2 and (i << 1) | 1 = i * 2 + 1
           self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) | 1]


   def update(self, i, x):
       i += self.N
       self.tree[i] = x
       while i > 1:
           self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
           i >>= 1
  
   # Query on [l, r) EXCLUSIVE
   def query(self, l, r):
       ans = 0
       l += self.N
       r += self.N
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

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixes = [(prefix, origin_i) for origin_i, prefix in enumerate([0] + list(accumulate(nums)))]
        prefixes.sort()
        pos = {origin_i: i for i, (_, origin_i) in enumerate(prefixes)}
        

        # need to find R such that 
        # lower + pref_sum[L - 1] <= prefix_sum[R] <= upper + pref_sum[L - 1]
        # 
        # sort the prefix_sum -> sorted_prefix = [(prefix_sum[i], i)]
        # conisder a K such that sorted_prefix[k] = (prefix_sum[j], j)
        # we need to find all k' such that sorted_prefix[k'] = (prefix_sum[i], i)
        # as j <= i so k' <= k

        ans = 0
        tree = SegmentTree([0] * len(prefixes))
        tree.update(pos[0], 1)
        for idx in range(1, len(prefixes)):
            prefix, origin_index = prefixes[idx]

            upper_target = prefix - upper
            lower_target = prefix - lower
            
            # print(lower_target, upper_target)

            r1 = bisect_left(prefixes, (upper_target, -inf))
            r2 = bisect_right(prefixes, (lower_target, inf)) - 1

            # print(r1, r2 + 1)
            # print(tree.query(r1, r2 + 1))
            ans += tree.query(r1, r2 + 1)
            tree.update(pos[origin_index], 1)

        return ans