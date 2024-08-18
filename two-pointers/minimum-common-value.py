class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = 0
        l2 = 0

        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] == nums2[l2]:
                return nums1[l1]
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1

        while l1 == len(nums1) and l2 < len(nums2):
            if nums1[-1] == nums2[l2]:
                return nums1[-1]
            else:
                l2 += 1

        while l2 == len(nums2) and l1 < len(nums1):
            if nums2[-1] == nums1[l1]:
                return nums2[-1]
            else:
                l1 += 1

        return -1