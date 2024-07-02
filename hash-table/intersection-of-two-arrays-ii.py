class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)

        ans = []
        for x in nums2:
            if d1[x] > 0:
                ans.append(x)
                d1[x] -= 1

        return ans