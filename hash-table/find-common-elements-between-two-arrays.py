class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        c1 = 0
        c2 = 0
        
        for x in nums1:
            if x in s2:
                c1 += 1
        
        for x in nums2:
            if x in s1:
                c2 += 1
                
        return [c1, c2]