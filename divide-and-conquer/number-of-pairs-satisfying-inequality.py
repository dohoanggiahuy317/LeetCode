class SegmentTree:
    def __init__(self, n):
        self.N = n
        self.tree = [0] * (self.N * 2)

    def update(self, i, val):
        i += self.N
        self.tree[i] = val
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def query(self, l, r):
        l += self.N
        r += self.N
        ans = 0

        while l < r:
            if l & 1:
                ans += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                ans += self.tree[r]
            
            l >>= 1
            r >>= 1
        
        return ans


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        li = [x - y for x, y in zip(nums1, nums2)]
        sorted_li = sorted([(subtract, i) for i, subtract in enumerate(li)])

        # need to find number of i, j such that li[i] - li[j] <= diff and i < j
        # fixed i
        # need to find number of j such that li[j] >= li[i] - diff
        # sorted_li = [(li[i], i), ...]
        # exist k such that sorted_li[k_i] = (li[i], i)
        # -> find the number of k' such that sorted_li[k_j] = (li[j], j)
        # as li[i] - diff <= li[j] -> binsearch to find k_j
        # 
        # create a segment tree to tell if we see index 0 -> k_j before?
        # -> loop backwards (at i) to find j a is in the right -> turn on the k_i of that i
        # to say that we meet this i -> so that we only check j on the right of i
        # when we query, we want to query (k_j, n) as we need to find num of sorted_li[k_j] >= sorted_li[k_i] + diff
        # update k_i to mark we all ready seen this index

        n = len(li)
        li2k = {}
        for k_i, (subtract, i) in enumerate(sorted_li):
            k_j = bisect_left(sorted_li, (subtract - diff, -inf))
            li2k[(subtract, i)] = (k_i, k_j)

        ans = 0
        tree = SegmentTree(n)
        for i in range(n - 1, -1, -1):
            subtract = li[i]
            k_i, k_j = li2k[(subtract, i)]
            ans += tree.query(k_j, n)
            tree.update(k_i, 1)
            
        return ans

