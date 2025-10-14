class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = 0, 0

        while i1 < m and i2 < n:
            if nums1[i1] <= nums2[i2]:
                i1 += 1
            else:
                prev = nums1[i1]
                for j in range(i1, m):
                    after = nums1[j + 1]
                    nums1[j + 1] = prev
                    prev = after
                nums1[i1] = nums2[i2]
                i1 += 1
                i2 += 1
        if i2 == n:
            return
        for j in range(i2, n):
            i1 += 1 if nums1[i1] != 0 else 0
            nums1[i1] = nums2[j]

