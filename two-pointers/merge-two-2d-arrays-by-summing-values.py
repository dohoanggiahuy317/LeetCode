class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)

        for id_, num in nums1:
            d[id_] += num

        for id_, num in nums2:
            d[id_] += num

        return sorted([list(ele) for ele in d.items()])