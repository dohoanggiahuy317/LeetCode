class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        ans = 0
        for i in range(len(nums1)):
            temp = 0

            j1 = i
            j2 = 0
            while j1 < len(nums1) and j2 < len(nums2):
                if nums1[j1] == nums2[j2]:
                    j1 += 1
                    j2 += 1
                    temp += 1
                else:
                    break

            ans = max(ans, temp)

        for i in range(len(nums2)):
            temp = 0

            j2 = i
            j1 = 0
            while j1 < len(nums1) and j2 < len(nums2):
                if nums1[j1] == nums2[j2]:
                    j1 += 1
                    j2 += 1
                    temp += 1
                else:
                    break

            ans = max(ans, temp)

        return ans