class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c_nums1 = Counter(nums1)
        c_nums2 = Counter(nums2)

        ans = []
        for num, freq in c_nums1.items():
            ans.extend([num] * min(freq, c_nums2[num]) )

        return ans