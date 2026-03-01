class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c_nums1 = Counter(nums1)
        ans = []

        for num in nums2:
            if c_nums1[num] > 0:
                result.append(num)
                c_nums1[num] -= 1

        return ans